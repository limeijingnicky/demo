from django.shortcuts import render
from booktest.models import BookInfo,HeroInfo
from django.db.models import F,Q,aggregates,Sum,Avg,Count,Max,Min
from django.views import View
from django.http import HttpResponse,JsonResponse
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from rest_framework.views import APIView
from booktest.serializers import BookInfoSerializer,HeroInfoSerializer,BookInfoModelSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.mixins import  ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView



# Create your views here.

##新增数据 save 方法
##save方法通过创建对象 创建表格
# book=BookInfo()
# book.btitle='三国演义'
# book.bpubdate='2021-03-22'
#
# book.save()

# book=BookInfo(
#     btitle='三国演义',
#     bpubdate='2021-03-22',
# )
# book.save()




##设置外键，可以直接连接对象名（连接该表对象的主键） hbook=book
##或者通过 id的方法，设置外键
# hero=HeroInfo(
#     htitle='队长',
#     hbook=book
# #    hbook_id=book_id
# )
# hero.save()


##新增数据 create方法
##create方法 直接通过类创建表格
# BookInfo.objects.create(
#     btitle='西游记',
#     bpubdate='2021-03-10',
# )


##查询
##get查询单一结果  all 所有结果 count 结果数量

##get方法
# try:
#     BookInfo.objects.get(id=10)
# except BookInfo.DoesNotExist:
#     print('查询失败')


##all 方法
# try:
#     BookInfo.objects.all()  ##返回一个 QuerySet
# except BookInfo.DoesNotExist:
#     print('查询失败')

##count方法
# try:
#     BookInfo.objects.all().count()  ##返回一个 QuerySet
# except BookInfo.DoesNotExist:
#     print('查询失败')


##过滤查询 filter exclude get
# #.filter(id=1) (btitle__contains='三') 双下划线   (btitle__endswith='三')  (btitle__startswith='三') (btitle__isnull=False)
##(id__in=[2,4]) 查询id为2和4  (id__gt=2)id大于2 (id__lt=3)小于3 (id__gte=2)大于等于2 (id__lte=2)大于等于2
##exclude(id=1) 不满足id=1条件的
##(bpubdate__year='2021') 年份为2021年
##(bpubdate__year__gt='2020') ##年份大于2020年的
##(bpubdate__gt='2021-03-10') ##日期大于'2021-03-10'的


##两个字段之间的比较查询
##比较bread阅读量和bcomment评论量两个字段的数据
#引入F对象(bread__gte=F('bcomment')) (bread__gte=F('bcomment')*2)还可以做算数运算

##逻辑运算
# 与 ， 将两个条件进行连接   (Q(bread__gt=1) ， Q(id__lt=2)) 或者 (bread__gt=1 ， id__lt=2)
# 或 |  将两个条件进行连接   (Q(bread__gt=1) | Q(id__lt=2))
# 非  ~ 满足条件以外（exclude一样） (~ Q(id__lt=2))



##聚合函数
##求字段的列数据 Avg Max Min Count Sum
##aggregate(Sum('bread')) 求和 {'bread__sum': 0}
##aggregate(Max('bread')) 求最大值 {'bread__max': 0}



##排序
##order_by ('bpubdate') 升序排列
##order_by('-bpubdate') 倒序排列


##关联查询
##外键是一个表中的一个字段，但也是另一个表中主键
#
#
# ##如果filter里的条件是当前模型内字段，而是关联模型的字段时，在字段名称前增加一个模型的名称 filter(heroinfo__htitle='队长')
# ##查询英雄表中htitlle字段为‘队长’的书
# BookInfo.objects.filter(heroinfo__htitle='队长')
# ##或者先查询英雄对象，再调用外键查询对应的书
# hero=HeroInfo.objects.get(htitle='队长')
# hero.hbook
#
#
#
# ##如果存在外键相关联，直接调用外键 filter(hbook_id=1) (hbook__btitle='三国演义')
# #查询书中btitle为‘三国演义’对应的英雄
# try:
#     HeroInfo.objects.filter(hbook__btitle='三国演义')
# except HeroInfo.DoesNotExist:
#     print('查询失败')
#
# #或者 先查询书，(btitle='三国演义') (id=1)
# # 再将对应在heroinfo中的所有信息进行查询  .heroinfo_set.all()
# try:
#     book=BookInfo.objects.get(btitle='三国演义')
#     book.heroinfo_set.all()
# except BookInfo.DoesNotExist:
#     print('查询失败')
#
#
#
# ##修改数据
# ##save方法
# try:
#     book=BookInfo.objects.get(btitle='三国演义2023')
#     book.btitle='三国演义'
#     print('已更改')
#     book.save()
# except BookInfo.DoesNotExist:
#     print('查询失败')
#
# ##update方法
# try:
#     BookInfo.objects.filter(btitle='三国演义2023').update(btitle='三国演义')
#     print('已更改')
# except BookInfo.DoesNotExist:
#     print('查询失败')
#
#
# ##删除数据
# ##delete,有关联关系的数据会一起删掉
# try:
#     book=BookInfo.objects.get(btitle='三国演义')
#     print('已更改')
#     book.delete()
# except BookInfo.DoesNotExist:
#     print('查询失败')
#
#
# ##filter（）。delete（）
# try:
#     BookInfo.objects.filter(btitle='西游记').delete()
#     print('已更改')
# except BookInfo.DoesNotExist:
#     print('查询失败')
#
# try:
#     book=BookInfo()
#     HeroInfo.objects.filter(htitle='队长',hgender=1,hbook_id=1).update(id=1)
#     print('已更改')
# except HeroInfo.DoesNotExist:
#     print('查询失败')
#






##REST framework
##对域名有一定的格式要求 books/id/
##返回请求值
#
#
# #使用DRF框架进行数据的增删改查实现
# class BookListAPIView(APIView):
#     #查询所有
#     def get(self,request):
#         qs=BookInfo.objects.all()
#         #调用序列化器,可以使用modelserializer 也可以使用自定的serializer
#         se=BookInfoModelSerializer(instance=qs,many=True)
#         # print(se)
#         # response=Response(se.data)
#         # print(response.data)    ##render以前的数据和序列化后的数据一样
#         # # print(response.content) ##得到render后的数据
#         #
#         # return response
#         ##drf里的请求和响应，不需要HTTPResponse或者JSONResponse… 可以直接响应为前端需要的格式
#         return Response(se.data)
#
#
#     ##新增
#     def post(self,request):
#         ##获取前端传入的请求
#         pdata=request.data
#         # 反序列化，将前端数据转换为模型
#         se=BookInfoModelSerializer(data=pdata)
#         #验证数据 is_valid
#         se.is_valid(raise_exception=True)
#         #使用序列化器的save方法，create新增
#         se.save()
#         #响应
#         return Response(se.data,status=status.HTTP_201_CREATED)
#
#
#
#
# class BookDetailAPIView(APIView):
#     ##查询单个
#     def get(self, request,pk):
#         try:
#             q = BookInfo.objects.get(id=pk)
#         except BookInfo.DoseNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         #使用序列化器
#         se=BookInfoModelSerializer(instance=q)
#         return Response(se.data)
#
#
#     ##更新单个
#     def put(self,request,pk):
#         try:
#             q=BookInfo.objects.get(id=pk)
#         except BookInfo.DoseNotExist:
#             return Response('there is no data',status=status.HTTP_404_NOT_FOUND)
#         re=request.data
#         se=BookInfoModelSerializer(instance=q,data=re)
#         se.is_valid(raise_exception=True)
#         se.save()
#         return Response(se.data)
#
#
#     ##删除单个
#     def delete(self,request,pk):
#         try:
#             q = BookInfo.objects.get(id=pk)
#         except BookInfo.DoseNotExist:
#             return Response('there is no data', status=status.HTTP_404_NOT_FOUND)
#         q.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#


#
#
# ##利用genericview方法,此方法继承于父类APIView
# class BookListGenericView(GenericAPIView):
#     ##指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     ##指定查询集
#     queryset = BookInfo.objects.all()  ##queryset和get_queryset相对应，一个存，一个取
#

    # #查询所有
    # def get(self,request):
    #     qs=self.get_queryset()
    #     se=self.get_serializer(qs,many=True)
    #     return Response(se.data)


    # def post(self, request):
    #     qs = self.get_queryset()
    #     se = self.get_serializer(data=qs)
    #     se.is_valid(raise_exception=True)
    #     se.save()
    #     return Response(se.data)

#
#
#
# class BookDetailGenericView(GenericAPIView):
#     serializer_class = BookInfoModelSerializer
#     queryset = BookInfo.objects.all()
#
#     def get(self,request,pk):
#         qs=self.get_object() #取单一对象,内部包含id=pk的操作
#         se=self.get_serializer(qs)
#         return Response(se.data)
#
#
#     def put(self,request,pk):
#         qs=self.get_object() ##拿到对象，如果错误会自动返回一个错误
#         se=self.get_serializer(instance=qs,data=request.data) ##反序列化
#         se.is_valid(raise_exception=True) #校验
#         se.save()
#         return Response(se.data,status=status.HTTP_201_CREATED)
#
#
#     def delete(self,request,pk):
#         qs=self.get_object() ##拿到对象，如果错误会自动返回一个错误
#         qs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



#
#
# ##利用mixin扩展类
# class BookListGenericView(ListModelMixin,CreateModelMixin,GenericAPIView):
#     ##指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     ##指定查询集
#     queryset = BookInfo.objects.all()  ##queryset和get_queryset相对应，一个存，一个取
#
#
#     #查询所有
#     def get(self,request):
#         ##mixin扩展类对以下代码进行了封装
#         # qs=self.get_queryset()
#         # se=self.get_serializer(qs,many=True)
#         # return Response(se.data)
#         return self.list(request)
#
#
#
#     def post(self, request):
#         ##mixin扩展类对以下代码进行了封装
#         # qs = self.get_queryset()
#         # se = self.get_serializer(data=qs)
#         # se.is_valid(raise_exception=True)
#         # se.save()
#         # return Response(se.data)
#         return self.create(request)
#
# #
#GenericAPIView函数，可以传递context属性，包含
# class BookDetailGenericView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
#     serializer_class = BookInfoModelSerializer
#     queryset = BookInfo.objects.all()
#
#     def get(self,request,pk):
#         ##mixin扩展类对以下代码进行了封装
#         # qs=self.get_object() #取单一对象,内部包含id=pk的操作
#         # se=self.get_serializer(qs)
#         # return Response(se.data)
#         return self.retrieve(request,pk)
#
#
#     def put(self,request,pk):
#         ##mixin扩展类对以下代码进行了封装
#         # qs=self.get_object() ##拿到对象，如果错误会自动返回一个错误
#         # se=self.get_serializer(instance=qs,data=request.data) ##反序列化
#         # se.is_valid(raise_exception=True) #校验
#         # se.save()
#         # return Response(se.data,status=status.HTTP_201_CREATED)
#         return self.update(request,pk)
#
#
#     def delete(self,request,pk):
#         ##mixin扩展类对以下代码进行了封装
#         # qs=self.get_object() ##拿到对象，如果错误会自动返回一个错误
#         # qs.delete()
#         # return Response(status=status.HTTP_204_NO_CONTENT)
#         return self.delete(request,pk)
#





# ##利用mixin扩展类
# class BookListGenericView(ListModelMixin,CreateModelMixin,GenericAPIView):
#     ##指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     ##指定查询集
#     queryset = BookInfo.objects.all()  ##queryset和get_queryset相对应，一个存，一个取
#
#
#     #查询所有
#     def get(self,request):
#         ##mixin扩展类对以下代码进行了封装
#         # qs=self.get_queryset()
#         # se=self.get_serializer(qs,many=True)
#         # return Response(se.data)
#         return self.list(request)
#
#
#
#     def post(self, request):
#         ##mixin扩展类对以下代码进行了封装
#         # qs = self.get_queryset()
#         # se = self.get_serializer(data=qs)
#         # se.is_valid(raise_exception=True)
#         # se.save()
#         # return Response(se.data)
#         return self.create(request)
#
#
#


#
# ##更简化
# class BookListGenericView(ListAPIView,CreateAPIView): ##ListCreateAPIView
#     ##指定序列化器类
#     serializer_class = BookInfoModelSerializer
#     ##指定查询集
#     queryset = BookInfo.objects.all()
#
#     ##ListAPIView类对以下代码进行了封装
#     # def get(self,request):
#     #     return self.list(request)
#
#     ##CreateAPIView类对以下代码进行了封装
#     # def post(self, request):
#     #     return self.create(request)
#
#
# class BookDetailGenericView(RetrieveAPIView,UpdateAPIView,DestroyAPIView): #RetrieveUpdateDestroyAPIView
#     serializer_class = BookInfoModelSerializer
#     queryset = BookInfo.objects.all()

    ##RetrieveAPIView类对以下代码进行了封装
    # def get(self,request,pk):
    #     return self.retrieve(request,pk)

    #UpdateAPIView类对以下代码进行了封装
    # def put(self,request,pk):
    #     return self.update(request,pk)

    # DestroyAPIView类对以下代码进行了封装
    # def delete(self,request,pk):
    #     return self.delete(request,pk)


##视图集的意义
''' 将所有接口写在一个类视图中，不再使用请求方法（get...），而是使用行为动作action（list...）
重写了as_view({'get':'list'})方法'''

from rest_framework.viewsets import ViewSet,GenericViewSet,ModelViewSet,ReadOnlyModelViewSet#(包含list 和 retrieve)
#ListModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,GenericViewSet)

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,BasePermission
from rest_framework.throttling import UserRateThrottle,ScopedRateThrottle
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django.db import DatabaseError
from rest_framework.views import exception_handler as drf_exception_handler
from django_filters.rest_framework import DjangoFilterBackend


##自定义权限
class Mypermission(BasePermission):
    ##访问当前所有方法list和detail的权限
    # def has_permission(self, request, view):
    #     return False

    ##访问当前detail的权限
    def has_object_permission(self, request, view, obj):
        return True

#自定义分页
class LargePagination(PageNumberPagination):
    page_size = 3 #默认每页显示几条
    max_page_size = 10 #前端可控制最大条
    page_query_param = 'page' #前端查询关键字，指定第几页 默认为page
    page_size_query_param = 'page_size' #前端查询关键字，指定每页条数,没有默认值


class LimitPagination(LimitOffsetPagination):
    default_limit = 3 #默认看几条
    max_limit = 10 #前端最多看几条
    limit_query_param = 'limit' #前端关键字，
    offset_query_param = 'offset' #前端关键字 偏移量:从第几条以后开始看






class BookViewSet(ModelViewSet):

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    ##主要作用在listview里，作为查询所有的过滤条件（？btitle=西游记）
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filter_fields = ['bread','bcomment']
    ordering_fields=['id','bread','bcomment']
    #排序过滤，查询
    # filter_backends = [OrderingFilter]
    # ordering_fields=['id','bread','bcomment']

    ##分页，查询
    pagination_class = LargePagination
    # pagination_class = LimitPagination

    ##指定当前视图访问的权限
    ##IsAuthenticated只有登录用户才能访问视图中的所有接口
    # permission_classes = [IsAuthenticated, Mypermission]
    ##IsAuthenticatedOrReadOnly 登录用户可读可写，不登录用户只可读
    # permission_classes = [IsAuthenticatedOrReadOnly]


    ##限流
    # throttle_classes = (UserRateThrottle,)
    # throttle_scope='bookview' ##在视图里，设置一个名称，对应settings文件里的设置 （'bookview': '1000/day'）


    #
    # @action(methods=['get'],detail=False)
    # def latest(self,request):
    #     qs=BookInfo.objects.latest('id')
    #     se= self.get_serializer(qs)
    #     return Response(se.data)
    #
    #
    # @action(methods=['put'],detail=True)
    # def read(self,request,pk):
    #     qs=self.get_object() ##自动读取pk值
    #     qs.bread=request.data.get('bread') ##修改某个属性
    #     qs.save()
    #     se=self.get_serializer(instance=qs)
    #     return Response(se.data)


#
# ##查询图书列表
# class BookListView(View):
#
#     ##查找所有图书接口
#     def get(self,request):
#         book_list=[]
#         booklist=BookInfo.objects.all()
#         for book in booklist:
#             book_dict= {
#             "id":book.id,
#             "btitle": book.btitle,
#             "bpubdate":book.bpubdate,
#             "bread":book.bread,
#             "bcomment":book.bcomment,
#             "image":book.image.url if book.image else ''
#             }
#             book_list.append(book_dict)
#         return JsonResponse(book_list,safe=False)

#
#  ##增加图书接口
#     def post(self, request):
#         #获取前端传入的请求数据
#         json_str_bytes=request.body
#         #将bytes转为字符串
#         json_str=json_str_bytes.decode()
#         #将json字符串转换为字典/列表
#         book_dict=json.loads(json_str)
#
#         ##将字典里值赋予表格对象，新增
#         book = BookInfo(
#             btitle= book_dict['btitle'],
#             bpubdate= book_dict['bpubdate']
#         )
#         book.save()
#
#         #将新增项目内容返回
#         json_dict = {
#             "id": book.id,
#             "btitle": book.btitle,
#             "bpubdate": book.bpubdate,
#             "bread": book.bread,
#             "bcomment": book.bcomment,
#             "image": book.image.url if book.image else ''
#         }
#
#         return JsonResponse(json_dict,status=201)  #指定响应状态为201
#
#
#
#
#
#
# ##查询图书单项
# class BookDetailView(View):
#
#     ##查找所单个图书接口
#     def get(self, request,pk):
#         try:
#             book= BookInfo.objects.get(id=pk)
#             book_dict = {
#                 "id": book.id,
#                 "btitle": book.btitle,
#                 "bpubdate": book.bpubdate,
#                 "bread": book.bread,
#                 "bcomment": book.bcomment,
#                 "image": book.image.url if book.image else ''
#             }
#             return JsonResponse(book_dict)
#         except BookInfo.DoesNotExist:
#             return HttpResponse('the id is over range',status=404)
#
#
#
#
#
#
#     ##修改所单个图书接口
#     def put(self,request,pk):
#
#         #查询对象
#         try:
#             book= BookInfo.objects.get(id=pk)
#
#             # 获取前端传入的数据
#             book_dict = json.loads(request.body.decode())
#
#             ##将字典里值赋予表格对象，更新数据
#             book.id=book_dict['id']
#             book.btitle=book_dict['btitle']
#             book.bpubdate=book_dict['bpubdate']
#             # book.bread= book_dict['bread'],
#             # book.bcomment= book_dict['bcomment'],
#             # book.image= book_dict['image']
#
#             book.save()
#
#             # 响应返回修改后的数据
#             json_dict = {
#                 "id": book.id,
#                 "btitle": book.btitle,
#                 "bpubdate": book.bpubdate,
#                 "bread": book.bread,
#                 "bcomment": book.bcomment,
#                 "image": book.image.url if book.image else ''
#             }
#             return JsonResponse(json_dict)
#         except BookInfo.DoesNotExist:
#             return HttpResponse('the id is over range',status=404)
#
#
#
#
#     ##删除所单个图书接口
#     def delete(self, request,pk):
#         try:
#             book= BookInfo.objects.get(id=pk)
#             # #直接删除数据，物理删除
#             # book.delete()
#
#             # #不删除数据，只改变属性，逻辑删除
#             book.bisdelete=True
#             book.save()
#
#             return HttpResponse('the id is deleted',status=204)  ##不用响应体，指定状态码为204
#
#         except BookInfo.DoesNotExist:
#             return HttpResponse('the id is over range',status=404)





# class BookInfoView(ModelViewSet):
#     #指定查询集
#     queryset = BookInfo.objects.all()
#
#     #指定序列化器
#     serializer_class = BookInfoSerializer


##序列化：将对象转换为json xml 字典等
##反序列化 ： 将json等 转换为对象模型


# ##查询模型对象
# book=BookInfo.objects.filter(id__gte=1)
# ##使用序列化器，输出json给前端
# ##如果需要对序列化器中的新增字段赋值，则直接book.bage=5
# s=BookInfoSerializer(instance=book) ##instance接收模型，当有个对象返回时，需要加上参数many=true
# s.data ##获得序列化后的数据
#
#
#
# ##关联序列化
# hero=HeroInfo.objects.get(id=1)
# ##带有外键时，默认输出主键的id
# s=HeroInfoSerializer(instance=hero) ##instance接收模型，当有个对象返回时，需要加上参数many=true
# s.data ##获得序列化后的数据
#
#
#
# data={
#     'id': 5,
#     'btitle':"巴黎圣母院",
#     'bpubdate':'2001-05-08',
#     'bread':'20',
#     'bcomment':'10'
# }

# ##手动定义反序列化
# # serializer= BookInfoSerializer(data=data) ##反序列化使用data 参数
# # serializer.is_valid(raise_exception=True) #校验数据是否符合要求 返回True false #raise_exception=True 可以自动抛出异常
# # serializer.errors ##获取校验后的错误信息
# # serializer.validated_data ##获取校验后正确的信息
# # serializer.data 可以直接获得序列化后的数据
#
