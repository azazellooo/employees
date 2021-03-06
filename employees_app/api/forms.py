from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'style': 'width: 300px;'})

    class Meta:
        model = Employee
        fields = ['name', 'last_name', 'age', 'department', 'programming_language']


