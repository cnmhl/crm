from django.shortcuts import render, redirect
from crm import models
from crm.forms.bj import BjModelForm
from crm.utils.pager import Pagination


def bj_list(request):
    """

    :param request:
    :return:
    """
    # 要查看的页码
    page = request.GET.get('page', 1)

    # 数据库中数据总条数

    total_count = models.ClassList.objects.all().count()

    #
    pager = Pagination(page, total_count, '/crm/bj/list/')
    bj_queryset = models.ClassList.objects.all()[pager.start:pager.end]
    return render(request, 'bj_list.html', {"bj_queryset": bj_queryset, 'pager': pager})


def bj_add(request):
    if request.method == 'GET':
        form = BjModelForm()
        return render(request, 'bj_form.html', {'form': form})
    form = BjModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/crm/bj/list/')
    return render(request, 'bj_form.html', {'form': form})


def bj_edit(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    obj = models.ClassList.objects.filter(id=nid).first()
    if request.method == "GET":
        # 生产HTML标签+携带默认值
        form = BjModelForm(instance=obj)
        print(form)
        return render(request, 'bj_form.html', {'form': form})  # 带默认值

    form = BjModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/bj/list/')
    return render(request, 'bj_form.html', {'form': form})


def bj_del(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    models.ClassList.objects.filter(id=nid).delete()
    return redirect('/crm/bj/list/')
