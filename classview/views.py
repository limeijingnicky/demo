from django.shortcuts import render,HttpResponse
from django.views import View
from django.utils.decorators import  method_decorator
from django.utils import timezone



##装饰器：主要作用是在不改变类的情况下，进行方法的修改和扩展
#对view_func进行方法的扩展 增加了一个wrapper函数
def my_decorator(view_func):

    def wrapper(request,*args,**kwargs):
        print('this is decorator')
        return view_func(request,*args,**kwargs)

    return wrapper


###方法是针对对象而言的函数，而函数可以是广泛使用的，因此方法在使用时需要注意self，在使用装饰器时使用method——decorator（）


# @method_decorator(my_decorator,name='post')
class DemoView(View):

    def get(self,request):
        print("这是get请求逻辑")
        return HttpResponse('get请求逻辑')

    # @method_decorator(my_decorator) ##在当前函数上直接标注就行
    def post(self,request):
        print("这是post请求逻辑")
        return HttpResponse('post请求逻辑')


##可以将方法赋给一个变量，之后通过这个变量广泛使用这个方法


##类多继承的特性，通过定义父类，让类视图集成这些扩展父类，实现代码的复用，通常以Mixin结尾命名这些父类




#创建模板
def template_demo(request):

    print('this is a template')

    ##需要渲染的数据为字典形式
    context={
        'city':'beijing',
        'alist': [1,2,3],
        'adict':{'age':40},

        'nowadate': timezone.now(),
        'ahtml':'<h1>大标题</h1>'

    }

    return render(request,template_name='index.html',context=context)


class Templatechild(View):

    def get(self,request):
        return render(request,'sonindex.html')




class JinjaTest(View):

    def get(self,request):

        print('this is Jinja2')

        ##需要渲染的数据为字典形式
        context={
            'city':'beijing',
            'alist': [120,220,320],
            'adict':{'age':40},

            'nowadate': timezone.now(),
            'ahtml':'<h1>大标题</h1>'

        }

        return render(request,template_name='jinja2_test.html',context=context)