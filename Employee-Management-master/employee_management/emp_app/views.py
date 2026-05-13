from datetime import datetime
from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department


# Create your views here.

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def index(request):
    return render(request, 'index.html')


def all(request):
    emps = Employee.objects.all()

    context = {
        'emps': emps
    }

    return render(request, 'view.html', context)


def add(request):

    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])

        # get selected ids from dropdown
        dept_id = request.POST['dept']
        role_id = request.POST['role']

        # fetch objects
        dept = Department.objects.get(id=dept_id)
        role = Role.objects.get(id=role_id)

        # create employee
        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            dept=dept,
            role=role,
            phone=phone,
            hire_date=datetime.now()
        )

        new_emp.save()

        return HttpResponse("Employee Added Successfully")

    elif request.method == "GET":

        departments = Department.objects.all()
        roles = Role.objects.all()

        context = {
            'departments': departments,
            'roles': roles
        }

        return render(request, "add.html", context)

    else:
        return HttpResponse("An exception occurred! Employee has not been added!")
    

def remove(request, emp_id=0):

    if emp_id:

        try:
            emp_delete = Employee.objects.get(id=emp_id)
            emp_delete.delete()

            return HttpResponse("Delete successful!")

        except Employee.DoesNotExist:
            return HttpResponse("Employee not found!")

        except Exception as e:
            return HttpResponse(f"Error: {e}")

    emps = Employee.objects.all()

    context = {
        'emps': emps
    }

    return render(request, 'remove.html', context)


def filter(request):
    return render(request, 'filter.html')
