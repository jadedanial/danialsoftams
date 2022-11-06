import django_tables2 as tables
from .models import *

class EmployeeTable(tables.Table):

    class Meta:
        model = Employee
        attrs = {"class": "search-result-table"}
        row_attrs = {'data-href': lambda record: record.get_absolute_url}
        fields = ['object_id', 'emp_name', 'emp_position', 'emp_salary', 'emp_dayoff', 'emp_shift', 'emp_remarks',]

class AttendanceTable(tables.Table):

    class Meta:
        model = Attendance
        attrs = {"class": "search-result-table"}
        row_attrs = {'data-href': lambda record: record.get_absolute_url}
        fields = ['object_id', 'attend_timein', 'attend_timeout', 'attend_date', 'attend_status', 'attend_remarks',]

class AssetTable(tables.Table):

    class Meta:
        model = Asset
        attrs = {"class": "search-result-table"}
        row_attrs = {'data-href': lambda record: record.get_absolute_url}
        fields = ['object_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area', 'asset_serial', 'asset_desc',]

class ChooseAssetTable(tables.Table):

    class Meta:
        model = Asset
        attrs = {"class": "search-result-table"}
        fields = ['object_id', 'asset_model', 'asset_type', 'asset_sector', 'asset_area',]

class RequestTable(tables.Table):

    class Meta:
        model = Request
        attrs = {"class": "search-result-table"}
        row_attrs = {'data-href': lambda record: record.get_absolute_url}
        fields = ['req_id', 'object_id', 'req_date', 'req_workshop', 'req_physloc', 'req_status', 'req_maint', 'req_repair', 'req_desc',]