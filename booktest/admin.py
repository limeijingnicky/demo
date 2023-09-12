from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

##编辑页面，关联展示Stacked 块的形式展示 TabularInline 表格的形式展示
class HeroInfoStack(admin.StackedInline):
    model=HeroInfo
    extra = 1


# Register your models here.
##需要model在admin站点中展示

class BookInfoAdmin(admin.ModelAdmin):
    ##调整界面
    actions_on_top=False
    actions_on_bottom=True

    list_per_page=2
    list_display = ['id','btitle','bpubdate','AddC','image'] ##默认为展示__str__方法，还可以使用其他的字段


    ##调整编辑界面
    # fields = ['btitle','bpubdate'] #设置可以编辑的字段

    fieldsets = [
        ['base',{'fields':['btitle','bpubdate','image']}],
        ['advanced',{'fields':['bread','bcomment'],
                   'classes':['collapse']}] ##cpollapse 设置网页折叠样式
    ]

    inlines = [HeroInfoStack]



class HeroInfoAdmin(admin.ModelAdmin):
    ##调整界面
    actions_on_top = False
    actions_on_bottom = True

    list_per_page = 2
    list_display = ['htitle','hbookx','hbookbread']  ##默认为展示__str__方法，还可以使用其他的字段


    ##设置admin界面右侧过滤侧栏
    list_filter = ['hbook','hgender']


    ##设置搜索框
    search_fields = ['htitle','hgender']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)

##对admin网页标题修改
admin.site.site_header='图书管理系统'
admin.site.site_title='tushu'
admin.site.index_title='欢迎使用图书管理系统'

