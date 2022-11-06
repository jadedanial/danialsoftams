from django.db import models
from django.urls import reverse

class Selection(models.Model):

    sel_name = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Selection Name')

    def __str__(self):
        return self.sel_name

class Parameter(models.Model):

    param_name = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Parameter Name')
    param_sel = models.ManyToManyField(Selection, blank = True, verbose_name = 'Selections')

    def __str__(self):
        return self.param_name

class Module(models.Model):

    mod_name = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Module Name')
    mod_url = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'URL')
    mod_param = models.ManyToManyField(Parameter, blank = True, verbose_name = 'Parameters')
    
    def __str__(self):
        return self.mod_name

class Section(models.Model):
    
    sec_name = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Section Name')
    sec_icon = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Icon')
    sec_mod = models.ManyToManyField(Module, blank = True, verbose_name = 'Modules')

    def __str__(self):
        return self.sec_name

class Employee(models.Model):

    object_id = models.IntegerField(blank = False, null = False, verbose_name = 'Employee ID')
    emp_name = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Name')
    emp_position = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Position')
    emp_salary = models.PositiveIntegerField(blank = False, null = False, verbose_name = 'Basic Salary')
    emp_dayoff = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Dayoff')
    emp_shift = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Shift')
    emp_remarks = models.CharField(max_length = 500, blank = True, null = True, verbose_name = 'Remarks')

    def __str__(self):
        return str(self.object_id)
    
    def get_absolute_url(self):
        return reverse('mod_update', kwargs={'category': 'employee', 'pk': self.pk})

class Attendance(models.Model):

    object_id = models.IntegerField(blank = False, null = False, verbose_name = 'Employee ID')
    attend_timein = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Time In')
    attend_timeout = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Time Out')
    attend_date = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Attendance Date')
    attend_status = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Attendance Status')
    attend_remarks = models.CharField(max_length = 500, blank = True, null = True, verbose_name = 'Remarks')

    def __str__(self):
        return str(self.object_id)

    def get_absolute_url(self):
        return reverse('mod_update', kwargs={'category': 'attendance', 'pk': self.pk})

class Asset(models.Model):

    object_id = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Asset ID')
    asset_model = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Model')
    asset_type = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Type')
    asset_sector = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Sector')
    asset_area = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Area')
    asset_serial = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Serial')
    asset_desc = models.TextField(blank = True, null = True, verbose_name = 'Description')

    def __str__(self):
        return self.object_id
    
    def get_absolute_url(self):
        return reverse('mod_update', kwargs={'category': 'asset', 'pk': self.pk})

class Request(models.Model):

    id = models.AutoField(primary_key = True)
    req_id = models.CharField(max_length = 500, blank = True, null = True, verbose_name = 'Work Request ID')
    object_id = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Asset ID')
    req_createby = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Created By')
    req_checkby = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Checked By')
    req_date = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Date')
    req_workshop = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Workshop')
    req_physloc = models.CharField(max_length = 500, blank = False, null = False, verbose_name = 'Physical Location')
    req_status = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Request Status')
    req_maint = models.CharField(max_length = 300, blank = True, null = True, verbose_name = 'Maintenance Type')
    req_repair = models.CharField(max_length = 300, blank = True, null = True, verbose_name = 'Repair Type')
    req_km = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'Kilometer')
    req_enghr = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'Engine Hour')
    req_fuel = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'Fuel Quantity')
    req_desc = models.TextField(blank = True, null = True, verbose_name = 'Description')

    def __str__(self):
        return self.req_asset
    
    def update_model(self):
        test_id = Request.objects.get(req_id = self.req_id).id
        Request.objects.filter(id = test_id).update(req_id = 'WR' + str(self.id))

    def save(self, *args, **kwargs):
        super(Request, self).save(*args, **kwargs)
        self.update_model()
    
    def get_absolute_url(self):
        return reverse('mod_update', kwargs={'category': 'workrequest', 'pk': self.pk})

