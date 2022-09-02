from django.db import models

class Selection(models.Model):

    sel_name = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Selection Name')

    def __str__(self):
        return self.sel_name

class Parameter(models.Model):

    param_name = models.CharField(max_length = 200, blank = False, null = False, verbose_name = 'Parameter Name')
    param_sel = models.ManyToManyField(Selection, blank = True, verbose_name = 'Parameter Selections')

    def __str__(self):
        return self.param_name

class Module(models.Model):

    mod_name = models.CharField(max_length = 200, blank = False, null = False, verbose_name = 'Module Name')
    mod_url = models.CharField(max_length = 200, blank = False, null = False, verbose_name = 'Module URL')
    mod_param = models.ManyToManyField(Parameter, blank = True, verbose_name = 'Module Parameters')
    
    def __str__(self):
        return self.mod_name

class Section(models.Model):
    
    sec_name = models.CharField(max_length = 200, blank = False, null = False, verbose_name = 'Section Name')
    sec_icon = models.CharField(max_length = 200, blank = False, null = False, verbose_name = 'Selection Icon')
    sec_mod = models.ManyToManyField(Module, blank = True, verbose_name = 'Selection Modules')

    def __str__(self):
        return self.sec_name

class Request(models.Model):

    id = models.AutoField(primary_key = True)
    req_code = models.CharField(max_length = 100, blank = True, null = True, editable = False, verbose_name = 'Request Code')
    req_asset = models.CharField(max_length = 300, verbose_name = 'Asset')
    req_date = models.DateField(verbose_name = 'Date')
    req_status = models.CharField(max_length = 300, verbose_name = 'Status')
    req_type = models.CharField(max_length = 300, verbose_name = 'Type')
    req_reptype = models.CharField(max_length = 300, verbose_name = 'Repair Type')
    req_workshop = models.CharField(max_length = 300, verbose_name = 'Workshop')
    req_description = models.TextField(verbose_name = 'Description')
    req_update = models.BooleanField(verbose_name = 'Update')

    def __str__(self):
        return self.req_asset
    
    def update_model(self):
        test_id = Request.objects.get(req_code = self.req_code).id
        Request.objects.filter(id = test_id).update(req_code = 'WR' + str(self.id))

    def save(self, *args, **kwargs):
        super(Request, self).save(*args, **kwargs)
        self.update_model()

class Employee(models.Model):

    emp_id = models.IntegerField(blank = False, null = False, verbose_name = 'Employee ID')
    emp_name = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Name')
    emp_position = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Position')
    emp_dayoff = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Dayoff')
    emp_shift = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Shift')
    emp_remarks = models.TextField(blank = True, null = True, verbose_name = 'Remarks')

    def __str__(self):
        return str(self.emp_id)

class Filter(models.Model):

    group_name = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Group Name')
    group_desc = models.TextField(blank = False, null = False, verbose_name = 'Description')
    filter_string = models.TextField(blank = False, null = False, verbose_name = 'Filter Text')
    group_sort = models.IntegerField(blank = False, null = False, verbose_name = 'Group Sort')

    def __str__(self):
        return self.group_name
    
class Template(models.Model):

    temp_name = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Template Name')
    temp_filter = models.ManyToManyField(Filter, blank = True, verbose_name = 'Filter')
    temp_default = models.BooleanField(blank = False, null = False, default = 'False', verbose_name = 'Set Default')

    def __str__(self):
        return self.temp_name

class Attendance(models.Model):

    emp_id = models.ForeignKey(Employee, on_delete = models.CASCADE, blank = False, null = False, verbose_name = 'Employee ID')
    attend_date = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Attendance Date')
    attend_timein = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Time In')
    attend_timeout = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Time Out')
    attend_status = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Attendance Status')
    attend_shiftfrom = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Shift From')
    attend_shiftto = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Shift To')

    def __str__(self):
        return str(self.emp_id)

class Order(models.Model):

    id = models.AutoField(primary_key = True)
    order_code = models.CharField(max_length = 100, blank = True, null = True, editable = False, verbose_name = 'Order Code')

    def __str__(self):
        return self.req_asset

class Asset(models.Model):

    asset_id = models.CharField(max_length = 10, blank = False, null = False, verbose_name = 'Asset Number')
    asset_model = models.CharField(max_length = 50, blank = False, null = False, verbose_name = 'Model')
    asset_type = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Type')
    asset_sector = models.CharField(max_length = 50, blank = False, null = False, verbose_name = 'Sector')
    asset_area = models.CharField(max_length = 50, blank = False, null = False, verbose_name = 'Area')
    asset_serial = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Serial')
    asset_desc = models.TextField(blank = True, null = True, verbose_name = 'Description')

    def __str__(self):
        return str(self.asset_id)