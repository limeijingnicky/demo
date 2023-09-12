##这个是当前功能下使用的路由（网址），解耦，使代码分离


from django.contrib import admin
#包含正则表达式的路径需要re_path方法

from django.urls import path,re_path
from . import views

urlpatterns = [
    ##url的正则名称
    path('homepage', views.home_page,name='homepage'),
    path('index',views.index),
    re_path(r'^weather/(?P<city>[a-z]+)/(?P<year>[0-9]+)',views.weather),
    re_path(r'^weather/$',views.get_query),
    re_path(r'^weather/get_form/$',views.get_form),
    re_path(r'^weather/get_json/$',views.get_json),
    re_path(r'^get_user/$',views.get_user),
    re_path(r'^response_json/$',views.response_json),
    re_path(r'^response_redirect/$',views.response_redirect),
    re_path(r'^response_cookies/$', views.cookie_demo),
    re_path(r'^response_session/$', views.session_demo),
]
