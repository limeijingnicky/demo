from django.db import models

##定义图书模型类

class BookInfo(models.Model):
    ##定义表单字段（属性）
    btitle=models.CharField(max_length=20,verbose_name='名称')
    bpubdate=models.DateField(verbose_name='发布日期')
    bread=models.IntegerField(default=0,verbose_name='阅读量')
    bcomment=models.IntegerField(default=0,verbose_name='评论量')
    bisdelete=models.BooleanField(default=0,verbose_name='逻辑删除')

    ##如果模型已经迁移建表，并且表中已经存在数据时，新添加的字段必须可以为null 或者包含默认值，否则迁移报错
    image=models.ImageField(verbose_name='图片',null=True,upload_to='book') ##表示图片将上传到MEDIA_ROOT里的book(自动创建的文件夹)里

    class Meta:
        db_table='tb_books' ##指明表单名
        verbose_name='图书' #在admin站点中显示名称
        verbose_name_plural=verbose_name ##显示负数名称

    def __str__(self):
        ##定义每个数据对象的显示信息
        return  self.btitle #只显示图书名称属性

    ##改善admin管理界面
    def AddC(self):
        if self.id==1:
            Ctitle=self.btitle+' '+'A'
        if self.id==2:
            Ctitle = self.btitle + ' ' + 'B'
        return Ctitle

    AddC.short_description='国内图书'
    AddC.admin_order_field='btitle'

##定义英雄模型类
class HeroInfo(models.Model):
    GENDER_CHOICES=(
        (0,'female'),
        (1,'male')
    )
    ##定义表单字段（属性）
    htitle = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    hdiscribe = models.CharField(max_length=20,null=True, verbose_name='描述信息') ##因为null默认为false 所以改为True
    hbook= models.ForeignKey(BookInfo,on_delete=models.CASCADE, verbose_name='图书') ##外键，从BookInfo表单，同时删除（CASCADE）
    hisdelete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'  ##指明表单名
        verbose_name = '英雄'  # 在admin站点中显示名称
        verbose_name_plural = verbose_name  ##显示负数名称

    def __str__(self):
        ##定义每个数据对象的显示信息
        return self.htitle  # 只显示英雄名称属性

    def hbookx(self):
        new_hbook=self.hbook
        return new_hbook

    def hbookbread(self):
        new_hbook_bread=self.hbook.bread
        return new_hbook_bread

    hbookx.short_description='关联图书'
    hbookx.admin_order_field = 'hbook_id'

    hbookbread.short_description = '关联图书阅读量'
    hbookbread.admin_order_field = 'hbook__bread'

#通过python manage.py makemigrations 命令对模型进行迁移

##迁移之后需要再实行命令行 python manage.py migrate 进行表格的建立





