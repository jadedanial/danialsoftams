from django.contrib import admin
from .models import *

class SelectionAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('id', 'sel_name',)
	list_filter = ('id', 'sel_name',)
	search_fields = ('id', 'sel_name',)

class ParameterAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('id', 'param_name',)
	list_filter = ('id', 'param_name',)
	search_fields = ('id', 'param_name',)

class ModuleAdmin(admin.ModelAdmin):
	
	readonly_fields = ('id',)
	list_display = ('id', 'mod_name', 'mod_url',)
	list_filter = ('id', 'mod_name', 'mod_url',)
	search_fields = ('id', 'mod_name', 'mod_url',)

class SectionAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('id', 'sec_name', 'sec_icon',)
	list_filter = ('id', 'sec_name', 'sec_icon',)
	search_fields = ('id', 'sec_name', 'sec_icon',)

class EmployeeAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('object_id', 'emp_name', 'emp_position', 'emp_salary', 'emp_dayoff', 'emp_shift', 'emp_remarks',)
	list_filter = ('object_id', 'emp_name', 'emp_position', 'emp_salary', 'emp_dayoff', 'emp_shift', 'emp_remarks',)
	search_fields = ('object_id', 'emp_name', 'emp_position', 'emp_salary', 'emp_dayoff', 'emp_shift', 'emp_remarks',)

class AttendanceAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('object_id', 'attend_date', 'attend_timein', 'attend_timeout', 'attend_status', 'attend_remarks',)
	list_filter = ('object_id', 'attend_date', 'attend_timein', 'attend_timeout', 'attend_status', 'attend_remarks',)
	search_fields = ('object_id', 'attend_date', 'attend_timein', 'attend_timeout', 'attend_status', 'attend_remarks',)

class AssetAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('object_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',)
	list_filter = ('object_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',)
	search_fields = ('object_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',)

class RequestAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('object_id', 'req_id', 'req_date', 'req_status', 'req_maint', 'req_repair', 'req_workshop', 'req_physloc', 'req_km', 'req_enghr', 'req_fuel', 'req_desc', 'req_checkby', 'req_createby',)
	list_filter = ('object_id', 'req_id', 'req_date', 'req_status', 'req_maint', 'req_repair', 'req_workshop', 'req_physloc', 'req_km', 'req_enghr', 'req_fuel', 'req_desc', 'req_checkby', 'req_createby',)
	search_fields = ('object_id', 'req_id', 'req_date', 'req_status', 'req_maint', 'req_repair', 'req_workshop', 'req_physloc', 'req_km', 'req_enghr', 'req_fuel', 'req_desc', 'req_checkby', 'req_createby',)

admin.site.register(Selection, SelectionAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Request, RequestAdmin)
