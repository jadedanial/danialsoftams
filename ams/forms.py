from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):

    fieldChoices, empposition, empdayoff, empshift = "", "", "", ""
    empPosition, empDayoff, empShift = (('', ''),), (('', ''),), (('', ''),)

    for p in Parameter.objects.values_list('param_name', flat=True):
        if p == 'Position' or p == 'Dayoff' or p == 'Shift':
            for parameter in Parameter.objects.filter(param_name = p).values_list('param_sel', flat=True):
                for selection in Selection.objects.filter(id = parameter).values_list('sel_name', flat=True):
                    fieldChoices += "(" + "\"" + str(selection) + "\"" + ", " + "\"" + str(selection) + "\"" + ")" + ", "
                    if p == 'Position':
                        empposition = fieldChoices
                    elif p == 'Dayoff':
                        empdayoff = fieldChoices
                    elif p == 'Shift':
                        empshift = fieldChoices
            fieldChoices = ""
    
    object_id = forms.CharField(label = "Employee ID", required = True, widget = forms.TextInput(attrs = {"class":"primary-input input-box-big input-field", "id":"object_id_input", "placeholder":"Employee ID", "autofocus":"true", "autocomplete":"off", "tabindex":"1"}))
    emp_name = forms.CharField(label = "Name", required = True, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"emp_name_input", "tabindex":"2", "onfocus":"(this.type='text')", "onchange":"showLabel('emp_name_label', 'emp_name_input', 'emp_name_clear')"}))
    empPosition += eval(empposition)
    emp_position = forms.ChoiceField(label = "Position", required = True, choices = empPosition, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"emp_position_input", "tabindex":"3", "onfocus":"(this.type='text')", "onchange":"showLabel('emp_position_label', 'emp_position_input', 'emp_position_clear')"}))
    emp_salary = forms.CharField(label = "Salary", required = True, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"emp_salary_input", "tabindex":"4", "onfocus":"(this.type='number')", "onchange":"showLabel('emp_salary_label', 'emp_salary_input', 'emp_salary_clear')"}))
    empDayoff += eval(empdayoff)
    emp_dayoff = forms.ChoiceField(label = "Dayoff", required = True, choices = empDayoff, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"emp_dayoff_input", "tabindex":"5", "onfocus":"(this.type='text')", "onchange":"showLabel('emp_dayoff_label', 'emp_dayoff_input', 'emp_dayoff_clear')"}))
    empShift += eval(empshift)
    emp_shift = forms.ChoiceField(label = "Shift", required = True, choices = empShift, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"emp_shift_input", "tabindex":"6", "onfocus":"(this.type='text')", "onchange":"showLabel('emp_shift_label', 'emp_shift_input', 'emp_shift_clear')"}))
    emp_remarks = forms.CharField(label = "Remarks", required = False, widget = forms.Textarea(attrs = {"class":"borderless-input input-field", "id":"emp_remarks_input", "rows":"5", "cols":"30", "tabindex":"7", "onfocus":"(this.type='text')", "onchange":"showLabel('emp_remarks_label', 'emp_remarks_input', 'emp_remarks_clear')"}))

    class Meta:
        model = Employee
        fields = ['object_id', 'emp_name', 'emp_position', 'emp_salary', 'emp_dayoff', 'emp_shift', 'emp_remarks',]

class AttendanceForm(forms.ModelForm):

    fieldChoices, atendstatus = "", ""
    attendStatus = (('', ''),)

    for p in Parameter.objects.values_list('param_name', flat=True):
        if p == 'Attendance Status':
            for parameter in Parameter.objects.filter(param_name = p).values_list('param_sel', flat=True):
                for selection in Selection.objects.filter(id = parameter).values_list('sel_name', flat=True):
                    fieldChoices += "(" + "\"" + str(selection) + "\"" + ", " + "\"" + str(selection) + "\"" + ")" + ", "
                    if p == 'Attendance Status':
                        atendstatus = fieldChoices
            fieldChoices = ""
    
    object_id = forms.CharField(label = "Employee ID", required = True, widget = forms.TextInput(attrs = {"class":"primary-input input-box-big input-field", "id":"object_id_input", "placeholder":"Employee ID", "autofocus":"true", "autocomplete":"off", "tabindex":"1"}))
    attend_timein = forms.CharField(label = "Time In", required = False, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"attend_timein_input", "tabindex":"2", "onfocus":"(this.type='time')", "onchange":"showLabel('attend_timein_label', 'attend_timein_input', 'attend_timein_clear')"}))
    attend_timeout = forms.CharField(label = "Time Out", required = False, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"attend_timeout_input", "tabindex":"3", "onfocus":"(this.type='time')", "onchange":"showLabel('attend_timeout_label', 'attend_timeout_input', 'attend_timeout_clear')"}))
    attend_date = forms.CharField(label = "Date", required = True, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"attend_date_input", "tabindex":"4", "onfocus":"(this.type='date')", "onchange":"showLabel('attend_date_label', 'attend_date_input', 'attend_date_clear')"}))
    attendStatus += eval(atendstatus)
    attend_status = forms.ChoiceField(label = "Status", required = True, choices = attendStatus, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"attend_status_input", "tabindex":"5", "onfocus":"(this.type='text')", "onchange":"showLabel('attend_status_label', 'attend_status_input', 'attend_status_clear')"}))
    attend_remarks = forms.CharField(label = "Remarks", required = False, widget = forms.Textarea(attrs = {"class":"borderless-input input-field", "id":"attend_remarks_input", "rows":"5", "cols":"30", "tabindex":"6", "onfocus":"(this.type='text')", "onchange":"showLabel('attend_remarks_label', 'attend_remarks_input', 'attend_remarks_clear')"}))

    class Meta:
        model = Attendance
        fields = ['object_id', 'attend_timein', 'attend_timeout', 'attend_date', 'attend_status', 'attend_remarks',]

class AssetForm(forms.ModelForm):

    fieldChoices, assetmodel, assettype, assetsector, assetarea = "", "", "", "", ""
    assetModel, assetType, assetSector, assetArea = (('', ''),), (('', ''),), (('', ''),), (('', ''),)

    for p in Parameter.objects.values_list('param_name', flat=True):
        if p == 'Model' or p == 'Type' or p == 'Sector' or p == 'Area':
            for parameter in Parameter.objects.filter(param_name = p).values_list('param_sel', flat=True):
                for selection in Selection.objects.filter(id = parameter).values_list('sel_name', flat=True):
                    fieldChoices += "(" + "\"" + str(selection) + "\"" + ", " + "\"" + str(selection) + "\"" + ")" + ", "
                    if p == 'Model':
                        assetmodel = fieldChoices
                    elif p == 'Type':
                        assettype = fieldChoices
                    elif p == 'Sector':
                        assetsector = fieldChoices
                    elif p == 'Area':
                        assetarea = fieldChoices
            fieldChoices = ""
    
    object_id = forms.CharField(label = "Asset ID", required = True, widget = forms.TextInput(attrs = {"class":"primary-input input-box-big input-field", "id":"object_id_input", "placeholder":"Asset ID", "autofocus":"true", "autocomplete":"off", "tabindex":"1"}))  
    assetModel += eval(assetmodel)
    asset_model = forms.ChoiceField(label = "Model", required = True, choices = assetModel, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"asset_model_input", "tabindex":"2", "onfocus":"(this.type='text')", "onchange":"showLabel('asset_model_label', 'asset_model_input', 'asset_model_clear')"}))
    assetType += eval(assettype)
    asset_type = forms.ChoiceField(label = "Type", required = True, choices = assetType, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"asset_type_input", "tabindex":"3", "onfocus":"(this.type='text')", "onchange":"showLabel('asset_type_label', 'asset_type_input', 'asset_type_clear')"}))
    assetSector += eval(assetsector)
    asset_sector = forms.ChoiceField(label = "Sector", required = True, choices = assetSector, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"asset_sector_input", "tabindex":"4", "onfocus":"(this.type='text')", "onchange":"showLabel('asset_sector_label', 'asset_sector_input', 'asset_sector_clear')"}))
    assetArea += eval(assetarea)
    asset_area = forms.ChoiceField(label = "Area", required = True, choices = assetArea, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"asset_area_input", "tabindex":"5", "onfocus":"(this.type='text')", "onchange":"showLabel('asset_area_label', 'asset_area_input', 'asset_area_clear')"}))
    asset_serial = forms.CharField(label = "Serial", required = False, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"asset_serial_input", "tabindex":"6", "onfocus":"(this.type='text')", "onchange":"showLabel('asset_serial_label', 'asset_serial_input', 'asset_serial_clear')"}))
    asset_desc = forms.CharField(label = "Description", required = False, widget = forms.Textarea(attrs = {"class":"borderless-input input-field", "id":"asset_desc_input", "rows":"5", "cols":"30", "tabindex":"7", "onfocus":"(this.type='text')", "onchange":"showLabel('asset_desc_label', 'asset_desc_input', 'asset_desc_clear')"}))

    class Meta:
        model = Asset
        fields = ['object_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',]

class RequestForm(forms.ModelForm):

    fieldChoices, reqmaint, reqrepair, reqworkshop, reqphysloc = "", "", "", "", ""
    reqMaint, reqRepair, reqWorkshop, reqPhysloc = (('', ''),), (('', ''),), (('', ''),), (('', ''),)

    for p in Parameter.objects.values_list('param_name', flat=True):
        if p == 'Maintenance Type' or p == 'Repair Type' or p == 'Workshop' or p == 'Physical Location':
            for parameter in Parameter.objects.filter(param_name = p).values_list('param_sel', flat=True):
                for selection in Selection.objects.filter(id = parameter).values_list('sel_name', flat=True):
                    fieldChoices += "(" + "\"" + str(selection) + "\"" + ", " + "\"" + str(selection) + "\"" + ")" + ", "
                    if p == 'Maintenance Type':
                        reqmaint = fieldChoices
                    elif p == 'Repair Type':
                        reqrepair = fieldChoices
                    elif p == 'Workshop':
                        reqworkshop = fieldChoices
                    elif p == 'Physical Location':
                        reqphysloc = fieldChoices
            fieldChoices = ""
    
    req_id = forms.CharField(label = "Work Request ID", required = False, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"req_id_input", "onfocus":"(this.type='text')", "onchange":"showLabel('req_id_label', 'req_id_input', 'req_id_clear')"}))
    object_id = forms.CharField(label = "Asset ID", required = True, widget = forms.TextInput(attrs = {"class":"primary-input input-box-big input-field", "id":"object_id_input", "placeholder":"Asset ID", "autofocus":"true", "autocomplete":"off", "tabindex":"1"}))
    req_createby = forms.CharField(label = "Created By", required = True, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"req_createby_input", "tabindex":"2", "onfocus":"(this.type='text')", "onchange":"showLabel('req_createby_label', 'req_createby_input', 'req_createby_clear')"}))
    req_checkby = forms.CharField(label = "Checked By", required = True, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"req_checkby_input", "tabindex":"3", "onfocus":"(this.type='text')", "onchange":"showLabel('req_checkby_label', 'req_checkby_input', 'req_checkby_clear')"}))
    req_date = forms.CharField(label = "Date", required = True, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"req_date_input", "tabindex":"4", "onfocus":"(this.type='date')", "onchange":"showLabel('req_date_label', 'req_date_input', 'req_date_clear')"}))
    reqWorkshop += eval(reqworkshop)
    req_workshop = forms.ChoiceField(label = "Workshop", required = True, choices = reqWorkshop, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"req_workshop_input", "tabindex":"5", "onfocus":"(this.type='text')", "onchange":"showLabel('req_workshop_label', 'req_workshop_input', 'req_workshop_clear')"}))
    reqPhysloc += eval(reqphysloc)
    req_physloc = forms.ChoiceField(label = "Physical Location", required = True, choices = reqPhysloc, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"req_physloc_input", "tabindex":"6", "onfocus":"(this.type='text')", "onchange":"showLabel('req_physloc_label', 'req_physloc_input', 'req_physloc_clear')"}))
    req_status = forms.CharField(label = "Request Status", required = True, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"req_status_input", "tabindex":"7", "onfocus":"(this.type='text')", "onchange":"showLabel('req_status_label', 'req_status_input', 'req_status_clear')"}))
    reqMaint += eval(reqmaint)
    req_maint = forms.ChoiceField(label = "Maintenance Type", required = True, choices = reqMaint, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"req_maint_input", "tabindex":"8", "onfocus":"(this.type='text')", "onchange":"showLabel('req_maint_label', 'req_maint_input', 'req_maint_clear')"}))
    reqRepair += eval(reqrepair)
    req_repair = forms.ChoiceField(label = "Repair Type", required = True, choices = reqRepair, widget = forms.Select(attrs = {"class":"custom-select-option input-field select-no-arrow", "id":"req_repair_input", "tabindex":"9", "onfocus":"(this.type='text')", "onchange":"showLabel('req_repair_label', 'req_repair_input', 'req_repair_clear')"}))
    req_km = forms.CharField(label = "Kilometer", required = True, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"req_km_input", "min":"1", "tabindex":"10", "onfocus":"(this.type='number')", "onchange":"showLabel('req_km_label', 'req_km_input', 'req_km_clear')"}))
    req_enghr = forms.CharField(label = "Engine Hour", required = False, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"req_enghr_input", "min":"1", "tabindex":"11", "onfocus":"(this.type='number')", "onchange":"showLabel('req_enghr_label', 'req_enghr_input', 'req_enghr_clear')"}))
    req_fuel = forms.CharField(label = "Fuel Quantity", required = False, widget = forms.TextInput(attrs = {"class":"borderless-input input-field", "id":"req_fuel_input", "min":"1", "tabindex":"12", "onfocus":"(this.type='number')", "onchange":"showLabel('req_fuel_label', 'req_fuel_input', 'req_fuel_clear')"}))
    req_desc = forms.CharField(label = "Description", required = False, widget = forms.Textarea(attrs = {"class":"borderless-input input-field", "id":"req_desc_input", "rows":"5", "cols":"30", "tabindex":"13", "onfocus":"(this.type='text')", "onchange":"showLabel('req_desc_label', 'req_desc_input', 'req_desc_clear')"}))

    class Meta:
        model = Request
        fields = ['req_id', 'object_id', 'req_createby', 'req_checkby', 'req_date', 'req_workshop', 'req_physloc', 'req_status', 'req_maint', 'req_repair', 'req_km', 'req_enghr', 'req_fuel', 'req_desc',]

