from django.conf.urls import url
from crm.views import home
from crm.views import depart
from crm.views import user
from crm.views import course
from crm.views import bj

urlpatterns = [
    url(r'^index/', home.index),
    url(r'^depart/list/$', depart.depart_list),
    url(r'^depart/add/$', depart.depart_add),
    url(r'^depart/edit/(\d+)/$', depart.depart_edit),
    url(r'^depart/del/(\d+)/$', depart.depart_del),

    url(r'^user/list/$', user.user_list),
    url(r'^user/add/$', user.user_add),
    url(r'^user/edit/(\d+)/$',user.user_edit),
    url(r'^user/del/(\d+)/$', user.user_del),

    url(r'^course/list/$', course.course_list),
    url(r'^course/add/$', course.course_add),
    url(r'^course/edit/(\d+)/$', course.course_edit),
    url(r'^course/del/(\d+)/$', course.course_del),

    url(r'^bj/list/$', bj.bj_list),
    url(r'^bj/add/$', bj.bj_add),
    url(r'^bj/edit/(\d+)/$', bj.bj_edit),
    url(r'^bj/del/(\d+)/$', bj.bj_del),

]