from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

def home(request):

    context = {
        'selections': Selection.objects.all(),
        'parameters': Parameter.objects.all(),
        'modules': Module.objects.all(),
        'sections': Section.objects.all(),
    }

    return render(request,"ams/home.html", context)

def module(request, category):

    context = {
        'selections': Selection.objects.all(),
        'parameters': Parameter.objects.all(),
        'modules': Module.objects.all(),
        'sections': Section.objects.all(),
        }

    if category == "workrequest":

        workrequest_list = Request.objects.all().order_by('-id').values()
        page = request.GET.get('page', 1)
        paginator = Paginator(workrequest_list, 10)

        try:
            workrequests = paginator.page(page)
        except PageNotAnInteger:
            workrequests = paginator.page(1)
        except EmptyPage:
            workrequests = paginator.page(paginator.num_pages)
        
        context = {
            'selections': Selection.objects.all(),
            'parameters': Parameter.objects.all(),
            'modules': Module.objects.all(),
            'sections': Section.objects.all(),
            'workrequests': workrequests,
        }

        return render(request,"ams/module/workrequest.html", context)
    
    elif category == "workorder":
        return render(request,"ams/module/workorder.html", context)
    
    elif category == "mileage":
        return render(request,"ams/module/mileage.html", context)
    
    elif category == "attendance":

        attendance_list = Attendance.objects.select_related('emp_id')
        page = request.GET.get('page', 1)
        paginator = Paginator(attendance_list, 31)

        try:
            attendances = paginator.page(page)
        except PageNotAnInteger:
            attendances = paginator.page(1)
        except EmptyPage:
            attendances = paginator.page(paginator.num_pages)

        employeeSearch = [{
            'id': '',
            'emp_id': '',
            'attend_date': '',
            'attend_timein': '',
            'attend_timeout': '',
            'attend_status': '',
            'attend_shiftfrom': '',
            'attend_shiftto': '',
        }]

        context = {
            'selections': Selection.objects.all(),
            'parameters': Parameter.objects.all(),
            'modules': Module.objects.all(),
            'sections': Section.objects.all(),
            'attendances': attendances,
            'employeesearch': employeeSearch,
        }

        if request.method == 'POST':

            if "employeesearch" in context: del context["employeesearch"]

            if request.POST.get("clear-button"):
                
                context["employeesearch"] = employeeSearch
            
            elif request.POST.get("update-from-cell-button"):

                empID = request.POST.get('cell-emp-id')
                attendDate = request.POST.get('cell-emp-date')
                updateToday = Attendance.objects.filter(emp_id__emp_id__exact = empID, attend_date = attendDate)

                messages.info(request, "Records found for employee ID " + str(empID) + " on date " + str(attendDate))
                context["employeesearch"] = updateToday
            
            else:
                
                empID = request.POST['employee-id']

                if empID != "" and empID.isnumeric():

                    attendDate = request.POST['attendance-date-input']
                    employeeExist = Employee.objects.filter(emp_id = empID).values()
                    attendedToday = Attendance.objects.filter(emp_id__emp_id__exact = empID, attend_date = attendDate)

                    if request.POST.get("save-button"):

                        attendTimein = request.POST['attendance-time-in-input']
                        attendTimeout = request.POST['attendance-time-out-input']
                        attendStatus = request.POST['Attendance Status-input']
                        attendShiftfrom = request.POST['shift-from-input']
                        attendShiftto = request.POST['shift-to-input']

                        if employeeExist:

                            if attendedToday:

                                attendedToday.update(
                                    attend_timein = attendTimein,
                                    attend_timeout = attendTimeout,
                                    attend_status = attendStatus,
                                    attend_shiftfrom = attendShiftfrom,
                                    attend_shiftto = attendShiftto,
                                )
                                
                                messages.info(request, "Employee ID " + str(empID) + " successfully updated.")
                            
                            else:
                                
                                attendance = Attendance(
                                    emp_id = Employee.objects.get(emp_id = empID),
                                    attend_date = attendDate,
                                    attend_timein = attendTimein,
                                    attend_timeout = attendTimeout,
                                    attend_status = attendStatus,
                                    attend_shiftfrom = attendShiftfrom,
                                    attend_shiftto = attendShiftto,
                                )
                                
                                attendance.save()
                                messages.info(request, "Employee ID " + str(empID) + " successfully saved.")
                            
                            context["employeesearch"] = [{
                                'id': '',
                                'emp_id': empID,
                                'attend_date': attendDate,
                                'attend_timein': attendTimein,
                                'attend_timeout': attendTimeout,
                                'attend_status': attendStatus,
                                'attend_shiftfrom': attendShiftfrom,
                                'attend_shiftto': attendShiftto,
                            }]

                        else:

                            messages.info(request, "No records found for employee ID " + str(empID))
                            context["employeesearch"] = [{
                                'id': '',
                                'emp_id': str(empID),
                                'attend_date': '',
                                'attend_timein': '',
                                'attend_timeout': '',
                                'attend_status': '',
                                'attend_shiftfrom': '',
                                'attend_shiftto': '',
                            }]
                    
                    elif request.POST.get("search-button"):

                        if employeeExist:

                            if attendDate != "" and attendDate != "mm/dd/yyyy":

                                if attendedToday:
                            
                                    messages.info(request, "Records found for employee ID " + str(empID) + " on date " + str(attendDate))
                                    context["employeesearch"] = attendedToday

                                else:

                                    messages.info(request, "Employee ID " + str(empID) + " not attended on date " + str(attendDate))
                                    context["employeesearch"] = [{
                                        'id': '',
                                        'emp_id': str(empID),
                                        'attend_date': attendDate,
                                        'attend_timein': '',
                                        'attend_timeout': '',
                                        'attend_status': '',
                                        'attend_shiftfrom': '',
                                        'attend_shiftto': '',
                                    }]
                                
                            else:
                                    
                                messages.info(request, "Please choose Attendance date.")
                                context["employeesearch"] = [{
                                    'id': '',
                                    'emp_id': str(empID),
                                    'attend_date': 'mm/dd/yyyy',
                                    'attend_timein': '',
                                    'attend_timeout': '',
                                    'attend_status': '',
                                    'attend_shiftfrom': '',
                                    'attend_shiftto': '',
                                }]

                        else:
                            
                            messages.info(request, "No records found for employee ID " + str(empID))
                            context["employeesearch"] = [{
                                'id': '',
                                'emp_id': str(empID),
                                'attend_date': '',
                                'attend_timein': '',
                                'attend_timeout': '',
                                'attend_status': '',
                                'attend_shiftfrom': '',
                                'attend_shiftto': '',
                            }]

                else:

                    messages.info(request, "ID should be numeric.")
                    context["employeesearch"] = [{
                        'id': '',
                        'emp_id': str(empID),
                        'attend_date': '',
                        'attend_timein': '',
                        'attend_timeout': '',
                        'attend_status': '',
                        'attend_shiftfrom': '',
                        'attend_shiftto': '',
                    }]

        return render(request,"ams/module/attendance.html", context)
    
    elif category == "shiftschedule":

        return render(request,"ams/module/shiftschedule.html", context)
    
    elif category == "assignshift":

        employeeSearch = [{
            'id': '',
            'emp_id': '',
            'emp_name': '',
            'emp_position': '',
            'emp_shift': '',
            'emp_dayoff': '',
            'emp_remarks': '',
        }]

        context = {
            'selections': Selection.objects.all(),
            'parameters': Parameter.objects.all(),
            'modules': Module.objects.all(),
            'sections': Section.objects.all(),
            'employees': Employee.objects.all(),
            'filters': Filter.objects.all(),
            'templates': Template.objects.all(),
            'employeesearch': employeeSearch,
        }

        if request.method == 'POST':

            if "employeesearch" in context: del context["employeesearch"]

            if request.POST.get("clear-button"):
                
                context["employeesearch"] = employeeSearch
            
            elif request.POST.get("employee-shift-template-input"):

                t = request.POST['employee-shift-template-input']
                tempSelect = Template.objects.filter(temp_name = t).values()

                if tempSelect:

                    for temp in Template.objects.all().iterator():
                        
                        tempNotSelect = Template.objects.filter(temp_name = temp.temp_name).values()
                        tempNotSelect.update(temp_default = "False")
                    
                    tempSelect.update(temp_default = "True")

                context["employeesearch"] = employeeSearch

            else:
                
                empID = request.POST['employee-id']

                if empID != "" and empID.isnumeric():

                    employeeExist = Employee.objects.filter(emp_id = empID).values()

                    if request.POST.get("save-button"):

                        empName = request.POST['employee-name-input']
                        empPosition = request.POST['employee-Position-input']
                        empShift = request.POST['employee-Shift-input']
                        empDayoff = request.POST['employee-Dayoff-input']
                        empRemarks = request.POST['employee-remarks-input']
                        
                        if employeeExist:

                            employeeExist.update(
                                emp_name = empName,
                                emp_position = empPosition,
                                emp_shift = empShift,
                                emp_dayoff = empDayoff,
                                emp_remarks = empRemarks,
                            )
                            
                            messages.info(request, "Employee ID " + str(empID) + " successfully updated.")
                            
                        else:

                            shift = Employee(
                                emp_id = empID,
                                emp_name = empName,
                                emp_position = empPosition,
                                emp_shift = empShift,
                                emp_dayoff = empDayoff,
                                emp_remarks = empRemarks,
                            )
                            
                            shift.save()
                            messages.info(request, "Employee ID " + str(empID) + " successfully saved.")
                            
                        context["employeesearch"] = [{
                            'id': '',
                            'emp_id': empID, 
                            'emp_name': empName,
                            'emp_position': empPosition,
                            'emp_shift': empShift,
                            'emp_dayoff': empDayoff,
                            'emp_remarks': empRemarks,
                        }]
                        
                    elif request.POST.get("search-button"):
                        
                        if employeeExist:
                            
                            messages.info(request, "Records found for employee ID " + str(empID))
                            context["employeesearch"] = employeeExist
                            
                        else:
                            
                            messages.info(request, "No records found for employee ID " + str(empID))
                            context["employeesearch"] = [{
                                'id': '',
                                'emp_id': str(empID), 
                                'emp_name': '',
                                'emp_position': '',
                                'emp_shift': '',
                                'emp_dayoff': '',
                                'emp_remarks': '',
                            }]

                else:

                    messages.info(request, "ID should be numeric.")
                    context["employeesearch"] = [{
                        'id': '',
                        'emp_id': str(empID), 
                        'emp_name': '',
                        'emp_position': '',
                        'emp_shift': '',
                        'emp_dayoff': '',
                        'emp_remarks': '',
                    }]

        return render(request,"ams/module/assignshift.html", context)
    
    elif category == "trackserialedpart":
        return render(request,"ams/module/trackserialedpart.html", context)
    
    elif category == "outofservice":
        return render(request,"ams/module/outofservice.html", context)
    
    elif category == "repaircost":
        return render(request,"ams/module/repaircost.html", context)
    
    elif category == "workorderstatus":
        return render(request,"ams/module/workorderstatus.html", context)
    
    elif category == "manhour":
        return render(request,"ams/module/manhour.html", context)
    
    elif category == "consumptionbypart":
        return render(request,"ams/module/consumptionbypart.html", context)
    
    elif category == "currentstock":
        return render(request,"ams/module/currentstock.html", context)
    
    elif category == "movestock":
        return render(request,"ams/module/movestock.html", context)
    
    elif category == "addstock":
        return render(request,"ams/module/addstock.html", context)
    
    elif category == "assets":
        return render(request,"ams/module/assets.html", context)