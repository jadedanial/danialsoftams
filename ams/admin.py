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

class RequestAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('id', 'req_code', 'req_date', 'req_status', 'req_type', 'req_reptype', 'req_workshop', 'req_description', 'req_update',)
	list_filter = ('id', 'req_code', 'req_date', 'req_status', 'req_type', 'req_reptype', 'req_workshop', 'req_description', 'req_update',)
	search_fields = ('id', 'req_code', 'req_date', 'req_status', 'req_type', 'req_reptype', 'req_workshop', 'req_description', 'req_update',)

class EmployeeAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('emp_id', 'emp_name', 'emp_position', 'emp_dayoff', 'emp_shift', 'emp_remarks',)
	list_filter = ('emp_id', 'emp_name', 'emp_position', 'emp_dayoff', 'emp_shift', 'emp_remarks',)
	search_fields = ('emp_id', 'emp_name', 'emp_position', 'emp_dayoff', 'emp_shift', 'emp_remarks',)

class FilterAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('id', 'group_name', 'group_desc', 'filter_string', 'group_sort',)
	list_filter = ('id', 'group_name', 'group_desc', 'filter_string', 'group_sort',)
	search_fields = ('id', 'group_name', 'group_desc', 'filter_string', 'group_sort',)

class TemplateAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('id', 'temp_name', 'temp_default',)
	list_filter = ('id', 'temp_name', 'temp_default',)
	search_fields = ('id', 'temp_name', 'temp_default',)

class AttendanceAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('emp_id', 'attend_date', 'attend_timein', 'attend_timeout', 'attend_status', 'attend_shiftfrom', 'attend_shiftto',)
	list_filter = ('emp_id', 'attend_date', 'attend_timein', 'attend_timeout', 'attend_status', 'attend_shiftfrom', 'attend_shiftto',)
	search_fields = ('emp_id', 'attend_date', 'attend_timein', 'attend_timeout', 'attend_status', 'attend_shiftfrom', 'attend_shiftto',)

class OrderAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('id', 'order_code',)
	list_filter = ('id', 'order_code',)
	search_fields = ('id', 'order_code',)

class AssetAdmin(admin.ModelAdmin):

	readonly_fields = ('id',)
	list_display = ('asset_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',)
	list_filter = ('asset_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',)
	search_fields = ('asset_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',)

admin.site.register(Selection, SelectionAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Asset, AssetAdmin)