import django_filters
from django.forms.widgets import TextInput
from .models import *

class EmployeeFilter(django_filters.FilterSet):

    object_id = django_filters.CharFilter(lookup_expr = "icontains", label = "Employee ID", widget = TextInput(attrs = {"class":"filter-field", "id":"object_id_filter", "placeholder":"Employee ID"}))
    emp_name = django_filters.CharFilter(lookup_expr = "icontains", label = "Name", widget = TextInput(attrs = {"class":"filter-field", "id":"emp_name_filter", "placeholder":"Name"}))
    emp_position = django_filters.CharFilter(lookup_expr = "icontains",label = "Position", widget = TextInput(attrs = {"class":"filter-field", "id":"emp_position_filter", "placeholder":"Position"}))
    emp_salary = django_filters.CharFilter(lookup_expr = "icontains", label = "Salary", widget = TextInput(attrs = {"class":"filter-field", "id":"emp_salary_filter", "placeholder":"Salary"}))
    emp_dayoff = django_filters.CharFilter(lookup_expr = "icontains", label = "Dayoff", widget = TextInput(attrs = {"class":"filter-field", "id":"emp_dayoff_filter", "placeholder":"Dayoff"}))
    emp_shift = django_filters.CharFilter(lookup_expr = "icontains", label = "Shift", widget = TextInput(attrs = {"class":"filter-field", "id":"emp_shift_filter", "placeholder":"Shift"}))
    emp_remarks = django_filters.CharFilter(lookup_expr = "icontains", label = "Remarks", widget = TextInput(attrs = {"class":"filter-field", "id":"emp_remarks_filter", "placeholder":"Remarks"}))

    class Meta:
        model = Employee
        fields = ['object_id', 'emp_name', 'emp_position', 'emp_salary', 'emp_dayoff', 'emp_shift', 'emp_remarks',]

class AttendanceFilter(django_filters.FilterSet):

    object_id = django_filters.CharFilter(lookup_expr = "icontains", label = "Employee ID", widget = TextInput(attrs = {"class":"filter-field", "id":"object_id_filter", "placeholder":"Employee ID"}))
    attend_timein = django_filters.CharFilter(lookup_expr = "icontains",label = "Time In", widget = TextInput(attrs = {"class":"filter-field", "id":"attend_timein_filter", "placeholder":"Time In"}))
    attend_timeout = django_filters.CharFilter(lookup_expr = "icontains", label = "Time Out", widget = TextInput(attrs = {"class":"filter-field", "id":"attend_timeout_filter", "placeholder":"Time Out"}))
    attend_date = django_filters.CharFilter(lookup_expr = "icontains", label = "Date", widget = TextInput(attrs = {"class":"filter-field", "id":"attend_date_filter", "placeholder":"Date"}))
    attend_status = django_filters.CharFilter(lookup_expr = "icontains", label = "Status", widget = TextInput(attrs = {"class":"filter-field", "id":"attend_status_filter", "placeholder":"Status"}))
    attend_remarks = django_filters.CharFilter(lookup_expr = "icontains", label = "Remarks", widget = TextInput(attrs = {"class":"filter-field", "id":"attend_remarks_filter", "placeholder":"Remarks"}))

    class Meta:
        model = Attendance
        fields = ['object_id', 'attend_timein', 'attend_timeout', 'attend_date', 'attend_status', 'attend_remarks',]

class AssetFilter(django_filters.FilterSet):

    object_id = django_filters.CharFilter(lookup_expr = "icontains", label = "Asset ID", widget = TextInput(attrs = {"class":"filter-field", "id":"object_id_filter", "placeholder":"Asset ID"}))
    asset_model = django_filters.CharFilter(lookup_expr = "icontains", label = "Model", widget = TextInput(attrs = {"class":"filter-field", "id":"asset_model_filter", "placeholder":"Model"}))
    asset_type = django_filters.CharFilter(lookup_expr = "icontains",label = "Type", widget = TextInput(attrs = {"class":"filter-field", "id":"asset_type_filter", "placeholder":"Type"}))
    asset_sector = django_filters.CharFilter(lookup_expr = "icontains", label = "Sector", widget = TextInput(attrs = {"class":"filter-field", "id":"asset_sector_filter", "placeholder":"Sector"}))
    asset_area = django_filters.CharFilter(lookup_expr = "icontains", label = "Area", widget = TextInput(attrs = {"class":"filter-field", "id":"asset_area_filter", "placeholder":"Area"}))
    asset_serial = django_filters.CharFilter(lookup_expr = "icontains", label = "Serial", widget = TextInput(attrs = {"class":"filter-field", "id":"asset_serial_filter", "placeholder":"Serial"}))
    asset_desc = django_filters.CharFilter(lookup_expr = "icontains", label = "Description", widget = TextInput(attrs = {"class":"filter-field", "id":"asset_desc_filter", "placeholder":"Description"}))

    class Meta:
        model = Asset
        fields = ['object_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',]

class RequestFilter(django_filters.FilterSet):

    req_id = django_filters.CharFilter(lookup_expr = "icontains", label = "Work Request ID", widget = TextInput(attrs = {"class":"filter-field", "id":"req_id_filter", "placeholder":"Request ID"}))
    object_id = django_filters.CharFilter(lookup_expr = "icontains", label = "Asset ID", widget = TextInput(attrs = {"class":"filter-field", "id":"object_id_filter", "placeholder":"Asset ID"}))
    req_createby = django_filters.CharFilter(lookup_expr = "icontains", label = "Created By", widget = TextInput(attrs = {"class":"filter-field", "id":"req_createby_filter", "placeholder":"Created By"}))
    req_checkby = django_filters.CharFilter(lookup_expr = "icontains", label = "Checked By", widget = TextInput(attrs = {"class":"filter-field", "id":"req_checkby_filter", "placeholder":"Checked By"}))
    req_date = django_filters.CharFilter(lookup_expr = "icontains", label = "Date", widget = TextInput(attrs = {"class":"filter-field", "id":"req_date_filter", "placeholder":"Date"}))
    req_workshop = django_filters.CharFilter(lookup_expr = "icontains", label = "Workshop", widget = TextInput(attrs = {"class":"filter-field", "id":"req_workshop_filter", "placeholder":"Workshop"}))
    req_physloc = django_filters.CharFilter(lookup_expr = "icontains", label = "Physical Location", widget = TextInput(attrs = {"class":"filter-field", "id":"req_physloc_filter", "placeholder":"Physical Location"}))
    req_status = django_filters.CharFilter(lookup_expr = "icontains", label = "Request Status", widget = TextInput(attrs = {"class":"filter-field", "id":"req_status_filter", "placeholder":"Request Status"}))
    req_maint = django_filters.CharFilter(lookup_expr = "icontains", label = "Maintenance Type", widget = TextInput(attrs = {"class":"filter-field", "id":"req_maint_filter", "placeholder":"Maintenance Type"}))
    req_repair = django_filters.CharFilter(lookup_expr = "icontains", label = "Repair Type", widget = TextInput(attrs = {"class":"filter-field", "id":"req_repair_filter", "placeholder":"Repair Type"}))

    class Meta:
        model = Request
        fields = ['req_id', 'object_id', 'req_createby', 'req_checkby', 'req_date', 'req_workshop', 'req_physloc', 'req_status', 'req_maint', 'req_repair',]