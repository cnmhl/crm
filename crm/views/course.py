from django.shortcuts import render, redirect
from crm import models
from crm.forms.course import CourseModelForm
from crm.utils.pager import Pagination


def course_list(request):
    """

    :param request:
    :return:
    """
    # 要查看的页码
    page = request.GET.get('page', 1)

    # 数据库中数据总条数

    total_count = models.Course.objects.all().count()

    #
    pager = Pagination(page, total_count, '/crm/course/list/')
    course_queryset = models.Course.objects.all()[pager.start:pager.end]
    return render(request, 'course_list.html', {"course_queryset": course_queryset, 'pager': pager})


def course_add(request):
    if request.method == 'GET':
        form = CourseModelForm()
        return render(request, 'course_form.html', {'form': form})
    form = CourseModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/crm/course/list/')
    return render(request, 'course_form.html', {'form': form})


def course_edit(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    obj = models.Course.objects.filter(id=nid).first()

    if request.method == "GET":
        # 生产HTML标签+携带默认值
        form = CourseModelForm(instance=obj)
        return render(request, 'course_form.html', {'form': form})  # 带默认值
    form = CourseModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/course/list/')
    return render(request, 'course_form.html', {'form': form})


def course_del(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    models.Course.objects.filter(id=nid).delete()
    return redirect('/crm/course/list/')
