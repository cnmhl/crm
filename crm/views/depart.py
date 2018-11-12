from django.shortcuts import render, redirect, HttpResponse
from crm import models
from django.forms import ModelForm
from django import forms
from crm.utils.pager import Pagination


class DepartModelForm(ModelForm):
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


# Create your views here.
def depart_list(request):
    """

    :param request:
    :return:
    """
    # 要查看的页码
    page = request.GET.get('page', 1)

    # 数据库中数据总条数

    total_count = models.Department.objects.all().count()

    #
    pager = Pagination(page, total_count, '/crm/depart/list/')

    depart_queryset = models.Department.objects.all()[pager.start:pager.end]
    return render(request, 'depart_list.html', {"depart_queryset": depart_queryset, 'pager': pager})


def depart_add(request):
    if request.method == 'GET':
        form = DepartModelForm()
        return render(request, 'depart_form.html', {'form': form})
    form = DepartModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/crm/depart/list/')
    return render(request, 'depart_form.html', {'form': form})


def depart_edit(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    obj = models.Department.objects.filter(id=nid).first()

    if request.method == "GET":
        # 生产HTML标签+携带默认值
        form = DepartModelForm(instance=obj)
        return render(request, 'depart_form.html', {'form': form})  # 带默认值
    form = DepartModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/depart/list/')
    return render(request, 'depart_form.html', {'form': form})


def depart_del(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    models.Department.objects.filter(id=nid).delete()
    return redirect('/crm/depart/list/')
