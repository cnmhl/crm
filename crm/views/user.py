from django.shortcuts import render, redirect
from crm import models
from crm.forms.user import UserModelForm
from crm.utils.pager import Pagination


def user_list(request):
    """

    :param request:
    :return:
    """
    # 要查看的页码
    page = request.GET.get('page', 1)

    # 数据库中数据总条数

    total_count = models.UserInfo.objects.all().count()

    #
    pager = Pagination(page, total_count, '/crm/user/list/')
    user_queryset = models.UserInfo.objects.all()[pager.start:pager.end]
    return render(request, 'user_list.html', {"user_queryset": user_queryset,'pager':pager})


def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_form.html', {'form': form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/crm/user/list/')
    return render(request, 'user_form.html', {'form': form})


def user_edit(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        # 生产HTML标签+携带默认值
        form = UserModelForm(instance=obj)
        return render(request, 'user_form.html', {'form': form})  # 带默认值
    form = UserModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/user/list/')
    return render(request, 'user_form.html', {'form': form})


def user_del(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/crm/user/list/')
