import json

from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse


# 创建首页
def home_page(request):

    print('this is home page')

    return HttpResponse('Home Page')


#创建分页
def index(request,city,year):
    print("this is index")

    return HttpResponse('this is index')


def weather(request,city,year):
    print("this is index")
    print(city)
    print(year)
    return HttpResponse(f'this is {city} in {year}')

##使用GET属性，获得网址路由中的参数？a=10 & b=30 获得QueryDict类型对象
def get_query(request):
    print("this is index")
    query=request.GET
    city=query.getlist('city')
    print(city)
    print(query)

    return HttpResponse(f'this is query')


##使用POST属性，获得表单数据 获得QueryDict类型对象
def get_form(request):
    print("this is get_form")
    query=request.POST
    city=query.getlist('city')
    print(city)
    print(query)

    return HttpResponse(f'this is query form')


##通过body属性，获得非表单类型数据
def get_json(request):
    print("this is get_json")
    json_bytes=request.body
    json_str=json_bytes.decode()
    dict=json.loads(json_str) #将json字符串转换为字典或者列表
    print(dict)

    return HttpResponse(f'this is query json')


##通过META的属性 获得请求头的信息
##method属性，表示请求使用的HTTP方法，包括‘GET’ ‘POST’


##user对象，获得当前用户对象
def get_user(request):
##没有登录，匿名用户对象 AnonymousUser
##登录，用户对象
    print(request.user)

    return HttpResponse('this is get_user')


##一般响应直接HttpResponse（content=‘’，content——type=‘’，status=200）
##响应json类
def response_json(request):
    # data={'city':'beijing','year':2017}
    # return JsonResponse(data)
##当数据为列表时，需要增加一个safe=False参数
    data = [{'city': 'beijing', 'year': 2017},123]
    return JsonResponse(data,safe=False)


##重定向redirect
def response_redirect(request):
    #当使用者为匿名用户时，将网页重定向到首页
    # if request.user is 'AnonymousUser':
    #     print('this is redirect')

    # return redirect('/homepage')

# ##反向解析视图函数view（homepage）网站网址为 /homepage 全局查找
#     redire=reverse('homepage')
#     print(redire)


    ##设置空间名称，缩小查找范围
    redire = reverse('users:homepage')
    print(redire)
    # return HttpResponse(redire)
    return redirect(redire)


###cookie 缓存在浏览器客户端,纯文本，键值对形式存储 session 缓存在服务器端(一般为redis数据库单独使用存储session) 可以缓存用户登录状态信息，购物车存储信息等等
##request是请求，前端发给后端的 response是响应，后端发给前端'
def cookie_demo(request):
    response=HttpResponse('cookies ok')
    response.set_cookie('name','nowaytol',max_age=360) ##时间单位秒
    response.set_cookie('password', '0000', max_age=360)  ##时间单位秒

    print(request.COOKIES.get('name'))
    print(request.COOKIES.get('password'))
    return response

##设置session session依赖于cookie，在session存储与redis时，生成一个session_id,会设置到cookies
def session_demo(request):
    # request.session['name']='nowaytol' #第一次设置时，是存储到redis数据库里
                                       #第二次读取时，是通过cookies里的session——id 读取redis数据库里数据

    print(request.session.get('name'))

    return HttpResponse('session ok')




