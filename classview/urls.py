from django.urls import path,include,re_path
from . import views


urlpatterns=[
    ##路由正则，函数名，路由别名
    re_path(r'^classview/$',views.my_decorator(views.DemoView.as_view())), ##装饰了DemoView下的所有方法
    re_path(r'^classview/$',views.DemoView.as_view()),
    # re_path(r'^classview/template/$',views.template_demo),
    re_path(r'^classview/template/child/$',views.Templatechild.as_view()),
    re_path(r'^classview/template/jinja2/$', views.JinjaTest.as_view()),
]