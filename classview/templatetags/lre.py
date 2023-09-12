from django import  template

#创建模板注册器
register=template.Library()

#定义过滤函数并添加装饰器把函数变为过滤器

@register.filter
def oddlre(ll):
    ll.reverse()
    print('this is reverse function')
    return ll


@register.filter
def oddlen(l):
    lenn=len(l)
    print('this is length function')
    return lenn