from crm import models
from django import forms


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'col-sm-10 form-control', 'placeholder': '用户名'}),
            'password': forms.TextInput(attrs={'class': 'col-sm-10 form-control', 'placeholder': '密码'}),
            'email': forms.EmailInput(attrs={'class': 'col-sm-10 form-control', 'placeholder': '邮箱'}),
            'gender': forms.Select(attrs={'class': 'col-sm-10 form-control'}),
            'depart': forms.Select(attrs={'class': 'col-sm-10 form-control'}),
        }
        error_messages = {
            'email': {
                'required': '邮箱不能为空',
                'invalid': '邮箱格式不对'
            }
        }
