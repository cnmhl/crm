from crm import models
from django import forms


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'col-sm-10 form-control', 'placeholder': '课程名称'})
        }
        error_messages = {
            'title': {
                'required': '课程名称不能为空'
            }
        }