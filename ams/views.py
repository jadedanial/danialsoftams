from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.export import TableExport
from django_tables2 import RequestConfig
from .models import *
from .forms import *
from .tables import *
from .filters import *

class HomeView(TemplateView):

    extra_context = {
        'selections': Selection.objects.all(),
        'parameters': Parameter.objects.all(),
        'modules': Module.objects.all(),
        'sections': Section.objects.all(),
        'urls': Module.objects.values_list('mod_url', flat=True),
    }
    template_name = 'ams/home.html'

class ModuleView(SingleTableMixin, FilterView):

    paginate_by = 10

    extra_context = {
        'selections': Selection.objects.all(),
        'parameters': Parameter.objects.all(),
        'modules': Module.objects.all(),
        'sections': Section.objects.all(),
    }
    template_name = 'ams/view.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ModuleView, self).get_context_data(*args,**kwargs)
        module = (self.kwargs['category'])
        context['mod'] = [{ 'mod_url':module,}]

        if module == 'employee':
            context['fields'] = [{
                'object_id_filter':'Employee ID',
                'emp_name_filter':'Name',
                'emp_position_filter':'Position',
                'emp_salary_filter':'Salary',
                'emp_dayoff_filter':'Dayoff',
                'emp_shift_filter':'Shift',
                'emp_remarks_filter':'Remarks',
            }]
        elif module == 'attendance':
            context['fields'] = [{
                'object_id_filter':'Employee ID',
                'attend_date_filter':'Date',
                'attend_timein_filter':'Time In',
                'attend_timeout_filter':'Time Out',
                'attend_status_filter':'Status',
                'attend_remarks_filter':'Remarks',
            }]
        elif module == 'asset':
            context['fields'] = [{
                'object_id_filter':'Asset ID',
                'asset_model_filter':'Model',
                'asset_type_filter':'Type',
                'asset_sector_filter':'Sector',
                'asset_area_filter':'Area',
                'asset_serial_filter':'Serial',
                'asset_desc_filter':'Description',
            }]
        elif module == 'workrequest':
            context['fields'] = [{
                'object_id_filter':'Asset ID',
                'req_id_filter':'Request ID',
                'req_date_filter':'Date',
                'req_status_filter':'Request Status',
                'req_maint_filter':'Maintenance Type',
                'req_repair_filter':'Repair Type',
                'req_workshop_filter':'Workshop',
                'req_physloc_filter':'Physical Location',
                'req_checkby_filter':'Checked By',
                'req_createby_filter':'Created By',
            }]

        return context
    
    def get(self, request, *args, **kwargs):

        module = (self.kwargs['category'])

        if module == 'employee':
            queryset = Employee.objects.all()
            table =  EmployeeTable(queryset)
        elif module == 'attendance':
            queryset = Attendance.objects.all()
            table =  AttendanceTable(queryset)
        elif module == 'asset':
            queryset = Asset.objects.all()
            table =  AssetTable(queryset)
        elif module == 'workrequest':
            queryset = Request.objects.all()
            table =  RequestTable(queryset)

        RequestConfig(request).configure(table)
        export_format = request.GET.get("_export", None)
    
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response("export.{}".format(export_format))

        return super().get(request, 'ams/view.html', {'table':table})

    def get_table_class(self):

        module = (self.kwargs['category'])

        if module == 'employee':
            return EmployeeTable
        elif module == 'attendance':
            return AttendanceTable
        elif module == 'asset':
            return AssetTable
        elif module == 'workrequest':
            return RequestTable
    
    def get_filterset_class(self):
        
        module = (self.kwargs['category'])

        if module == 'employee':
            return EmployeeFilter
        elif module == 'attendance':
            return AttendanceFilter
        elif module == 'asset':
            return AssetFilter
        elif module == 'workrequest':
            return RequestFilter

class ModuleCreate(SuccessMessageMixin, SingleTableMixin, CreateView):

    paginate_by = 5

    extra_context = {
        'selections': Selection.objects.all(),
        'parameters': Parameter.objects.all(),
        'modules': Module.objects.all(),
        'sections': Section.objects.all(),
    }
    template_name = 'ams/create.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ModuleCreate, self).get_context_data(*args,**kwargs)
        module = (self.kwargs['category'])
        context['mod'] = [{ 'mod_url':module,}]

        if module == 'employee':
            context['fieldgroups'] = [
                {
                    'name':'EMPLOYEE INFO',
                    'id':'employee-info',
                    'fields':['emp_name', 'emp_position', 'emp_salary',]
                },
                {
                    'name':'SCHEDULE',
                    'id':'employee-schedule',
                    'fields':['emp_dayoff', 'emp_shift',]
                },
                {
                    'name':'REMARKS',
                    'id':'employee-remarks',
                    'fields':['emp_remarks',]
                },
            ]
        elif module == 'attendance':
            context['fieldgroups'] = [
                {
                    'name':'ATTENDANCE INFO',
                    'id':'attendance-info',
                    'fields':['attend_timein', 'attend_timeout', 'attend_date', 'attend_status',]
                },
                {
                    'name':'REMARKS',
                    'id':'attendance-remarks',
                    'fields':['attend_remarks',]
                },
            ]
        elif module == 'asset':
            context['fieldgroups'] = [
                {
                    'name':'ASSET INFO',
                    'id':'asset-info',
                    'fields':['asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial',]
                },
                {
                    'name':'DESCRIPTION',
                    'id':'asset-description',
                    'fields':['asset_desc',]
                },
            ]
        elif module == 'workrequest':
            context['fieldgroups'] = [
                {
                    'name':'WORK REQUEST INFO',
                    'id':'work-request-info',
                    'fields':[{'field':'req_id', 'value':'', 'readonly':'yes'}, {'field':'req_createby', 'value':self.request.user, 'readonly':'yes'}, {'field':'req_checkby', 'value':'', 'readonly':'no'}, {'field':'req_date', 'value':'', 'readonly':'no'},]
                },
                {
                    'name':'STATUS AND TYPE',
                    'id':'status-and-type',
                    'fields':[{'field':'req_workshop', 'value':'', 'readonly':'no'}, {'field':'req_physloc', 'value':'', 'readonly':'no'}, {'field':'req_status', 'value':'New', 'readonly':'yes'}, {'field':'req_maint', 'value':'', 'readonly':'no'}, {'field':'req_repair', 'value':'', 'readonly':'no'},]
                },
                {
                    'name':'METERS',
                    'id':'meters-info',
                    'fields':[{'field':'req_km', 'value':'', 'readonly':'no'}, {'field':'req_enghr', 'value':'', 'readonly':'no'}, {'field':'req_fuel', 'value':'', 'readonly':'no'},]
                },
                {
                    'name':'DESCRIPTION',
                    'id':'request-description',
                    'fields':[{'field':'req_desc', 'value':'', 'readonly':'no'},]
                },
            ]

        return context
    
    def get_queryset(self):

        module = (self.kwargs['category'])

        if module == 'workrequest':
            queryset = Asset.objects.all()

        return queryset

    def get_table_class(self):

        module = (self.kwargs['category'])

        if module == 'workrequest':
            return ChooseAssetTable

    def get_form_class(self):

        module = (self.kwargs['category'])

        if module == 'employee':
            return EmployeeForm
        elif module == 'attendance':
            return AttendanceForm
        elif module == 'asset':
            return AssetForm
        elif module == 'workrequest':
            return RequestForm

    def form_valid(self, form):

        module = (self.kwargs['category'])

        if module == 'employee' or module == 'asset':

            if module == 'employee':
                model = Employee
                subject = 'Employee ID '
            elif module == 'asset':
                model = Asset
                subject = 'Asset ID '

            objectID = form.cleaned_data['object_id']
            defaults = {}
        
            for f in form.cleaned_data:
                defaults[f] = form.cleaned_data[f]
            
            if 'object_id' in defaults: del defaults['object_id']

            try:
                obj = model.objects.get(object_id = objectID)
                for key, value in defaults.items():
                    setattr(obj, key, value)
                    obj.save()
                message = subject + objectID + ' successfully saved.'
            except model.DoesNotExist:
                new_values = {'object_id': objectID,}
                new_values.update(defaults)
                obj = model(**new_values)
                obj.save()
                message = subject + objectID + ' successfully saved.'

        elif module == 'attendance':

            model = Attendance

            objectID = form.cleaned_data['object_id']
            defaults = {}
        
            for f in form.cleaned_data:
                defaults[f] = form.cleaned_data[f]
            
            if 'object_id' in defaults: del defaults['object_id']

            if Employee.objects.filter(object_id = form.cleaned_data['object_id']):

                try:
                    obj = model.objects.get(object_id = objectID, attend_date = form.cleaned_data['attend_date'])
                    for key, value in defaults.items():
                        setattr(obj, key, value)
                        obj.save()
                    message = 'Attendance for Employee ID ' + objectID + ' successfully saved.'
                except model.DoesNotExist:
                    new_values = {'object_id': objectID,}
                    new_values.update(defaults)
                    obj = model(**new_values)
                    obj.save()
                    message = 'Attendance for Employee ID ' + objectID + ' successfully saved.'
            
            else:

                message = 'Employee ID ' + objectID + ' does not exist.'

        elif module == 'workrequest':

            model = Request

            reqID = form.cleaned_data['req_id']
            objectID = form.cleaned_data['object_id']
            defaults = {}
        
            for f in form.cleaned_data:
                defaults[f] = form.cleaned_data[f]
            
            if 'req_id' in defaults: del defaults['req_id']

            if Asset.objects.filter(object_id = form.cleaned_data['object_id']):

                try:
                    req = model.objects.get(req_id = reqID)
                    for key, value in defaults.items():
                        setattr(req, key, value)
                        req.save()
                    message = 'Work Request ID ' + 'WR' + str(req.id) + ' successfully saved.'
                except model.DoesNotExist:
                    new_values = {'req_id': reqID,}
                    new_values.update(defaults)
                    req = model(**new_values)
                    req.save()
                    message = 'Work Request ID ' + 'WR' + str(req.id) + ' successfully saved.'
            
            else:

                message = 'Asset ID ' + objectID + ' does not exist.'

        context = self.get_context_data(form = form)
        context['form_message'] = [{ 'message': message,}]
        context['request_id'] = [{ 'requestID': 'WR' + str(req.id),}]
        return self.render_to_response(context = context)
    
    def form_invalid(self, form):

        context = self.get_context_data(form = form)
        context['form_message'] = [{ 'message': 'Invalid, please check input fields!',}]
        print(form.errors.as_data())
        return self.render_to_response(context = context)

class ModuleUpdate(SuccessMessageMixin, UpdateView):

    extra_context = {
        'selections': Selection.objects.all(),
        'parameters': Parameter.objects.all(),
        'modules': Module.objects.all(),
        'sections': Section.objects.all(),
    }
    template_name = 'ams/create.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ModuleUpdate, self).get_context_data(*args,**kwargs)
        module = (self.kwargs['category'])
        context['mod'] = [{ 'mod_url':module,}]

        return context
    
    def get_object(self, queryset = None):

        module = (self.kwargs['category'])

        if module == 'employee':
            model = Employee
        elif module == 'attendance':
            model = Attendance
        elif module == 'asset':
            model = Asset

        obj = model.objects.get(id = self.kwargs['pk'])

        return obj

    def get_form_class(self):

        module = (self.kwargs['category'])

        if module == 'employee':
            return EmployeeForm
        elif module == 'attendance':
            return AttendanceForm
        elif module == 'asset':
            return AssetForm

    def form_valid(self, form):

        module = (self.kwargs['category'])

        if module == 'employee' or module == 'asset':

            if module == 'employee':
                model = Employee
                subject = 'Employee ID '
            elif module == 'asset':
                model = Asset
                subject = 'Asset ID '

            objectID = form.cleaned_data['object_id']
            defaults = {}
        
            for f in form.cleaned_data:
                defaults[f] = form.cleaned_data[f]
            
            if 'object_id' in defaults: del defaults['object_id']

            try:
                obj = model.objects.get(object_id = objectID)
                for key, value in defaults.items():
                    setattr(obj, key, value)
                    obj.save()
                message = subject + objectID + ' successfully saved.'
            except model.DoesNotExist:
                new_values = {'object_id': objectID,}
                new_values.update(defaults)
                obj = model(**new_values)
                obj.save()
                message = subject + objectID + ' successfully saved.'

        elif module == 'attendance':

            model = Attendance

            objectID = form.cleaned_data['object_id']
            defaults = {}
        
            for f in form.cleaned_data:
                defaults[f] = form.cleaned_data[f]
            
            if 'object_id' in defaults: del defaults['object_id']

            if Employee.objects.filter(object_id = form.cleaned_data['object_id']):

                try:
                    obj = model.objects.get(object_id = objectID, attend_date = form.cleaned_data['attend_date'])
                    for key, value in defaults.items():
                        setattr(obj, key, value)
                        obj.save()
                    message = 'Attendance for Employee ID ' + objectID + ' successfully saved.'
                except model.DoesNotExist:
                    new_values = {'object_id': objectID,}
                    new_values.update(defaults)
                    obj = model(**new_values)
                    obj.save()
                    message = 'Attendance for Employee ID ' + objectID + ' successfully saved.'
            
            else:

                message = 'Employee ID ' + objectID + ' does not exist.'

        context = self.get_context_data(form = form)
        context['form_message'] = [{ 'message': message,}]
        return self.render_to_response(context = context)
    
    def form_invalid(self, form):

        context = self.get_context_data(form = form)
        context['form_message'] = [{ 'message': 'Invalid, please check input fields!',}]
        return self.render_to_response(context = context)