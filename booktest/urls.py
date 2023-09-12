from django.urls import path,include,re_path
from booktest import views
from rest_framework.routers import DefaultRouter


urlpatterns=[
    # ##路由正则，函数名，路由别名
    # re_path(r'^books/$',views.BookListView.as_view(),name='booklist'),
    # re_path(r'^books/(?P<pk>\d+)/$',views.BookDetailView.as_view(),name='bookdetail'),

    # re_path(r'^books/$',views.BookListAPIView.as_view(),name='booklistapi'),
    # re_path(r'^books/(?P<pk>\d+)/$',views.BookDetailAPIView.as_view(),name='bookdetailapi'),

    # re_path(r'^books/$', views.BookListGenericView.as_view(), name='booklistapi'),
    #     # re_path(r'^books/(?P<pk>\d+)/$', views.BookDetailGenericView.as_view(), name='bookdetailapi'),

    # re_path(r'^books/$', views.BookViewSet.as_view({'get': 'list','post': 'create'}), name='booklistapi'),
    # re_path(r'^books/(?P<pk>\d+)/$', views.BookViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'}), name='bookdetailapi'),


    # #如果有其它行为
    # re_path(r'^books/latest/$', views.BookViewSet.as_view({'get': 'latest'}), name='booklateapi'),#将get方法指定为自定的方法，并且路由需要重新写
    # re_path(r'^books/(?P<pk>\d+)/read/$', views.BookViewSet.as_view({'put': 'update'}), name='bookreadapi'),


]


#自动生成基本路由,对应modelviewset时，5个action,配合视图集（viewset）使用时,自动生成带有其他行为的路由
router=DefaultRouter() ##自动生成一个跟路由 http://127.0.0.1:8000/
router.register(r'books', views.BookViewSet,basename='bookinfo')

urlpatterns+=router.urls




