from crm import models
from django import forms


class BjModelForm(forms.ModelForm):
    class Meta:
        model = models.ClassList
        fields = '__all__'
        widgets = {
            'course': forms.Select(attrs={'class': 'col-sm-10 form-control'}),
            'num': forms.TextInput(attrs={'class': 'col-sm-10 form-control', 'placeholder': '第几期'}),
            'teacher': forms.SelectMultiple(attrs={'class': 'col-sm-10 form-control'}),
        }
        error_messages = {
            'num': {
                'required': '此列不能为空',
            }
        }