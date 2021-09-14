from django.shortcuts import render,redirect
from .models import Employee
from .form import Employeeform

# Create your views here.
def home(request):
    return render(request,'welcome.html')

def load_form(request):
    form=Employeeform()
    return render(request,'index.html',{'form':form})

def add(request):
     if request.method=='POST':
        form=Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crudapp/add')
     form=Employeeform()
     return render(request,'confirmation.html',{'form':form})

def show(request):
    employee=Employee.objects.all()
    return render(request,'show.html',{'employee':employee})

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=Employeeform(request.POST,instance=employee)
    form.save()
    return redirect('/crudapp/show')

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/crudapp/show')

def search(request):
    given_name=request.POST['name']
    employee = Employee.objects.filter(ename__icontains=given_name)
    return render(request,'show.html',{'employee': employee})

