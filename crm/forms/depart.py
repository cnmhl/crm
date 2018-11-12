from crm import models
from django import forms


class DepartModelForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'col-sm-10 form-control', 'placeholder': '部门名称'})
        }
        error_messages = {
            'title': {
                'required': '部门名称不能为空'
            }
        }