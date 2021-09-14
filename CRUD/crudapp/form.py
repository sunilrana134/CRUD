from django import forms

# import my_Model from models.py
from .models import Employee


# create a ModelForm
class Employeeform(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Employee
        fields = "__all__"