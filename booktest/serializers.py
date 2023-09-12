from rest_framework import serializers
from booktest.models import BookInfo,HeroInfo



class BookInfoModelSerializer(serializers.ModelSerializer):
    ##由于继承于父类serializers，可以增加字段
    # password=serializers.CharField()

    ##定义序列化器，可以自动生成模型中的字段
    ##自动实现了create 和 update
    class Meta:
        model=BookInfo #指定映射模型
        fields='__all__' #指定映射字段
        extra_kwargs={
            'id':{'required': False},
            'btitle': {'required': False},#修改字段中的参数的默认值
            'bpubdate': {'required': False},
            'bcomment': {'required': False}
        }
        # fields=['id','btitle','bpubdate','password'] ##映射指定字段
        # exclude= ['image']##除了image 其他字段均映射
    #
        # extra_kwargs={
        #     'bread':{'min_value':0}, #修改字段中的参数的默认值
        #     'bcomment':{'min_value':0,'write_only':True}
        # }
    #     read_only_fields=['bread'] ##可以指定只读字 段


#或者将校验方法写在类别之外，与validators配合使用,并且可以同时校验多个字段
# def vv(value):
#     if 'dd' not in value.lower():
#         raise serializers.ValidationError('there is not related to dd')
#     return value



#手动实现序列化器
class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID') #read_only默认为false
    btitle = serializers.CharField(max_length=20, label='名称',required=True)#,validators=[vv]) # required 默认为true
    bpubdate = serializers.DateField(label='发布日期') # required 默认为true
    bread = serializers.IntegerField(label='阅读量',required=False)
    bcomment = serializers.IntegerField(label='评论量',required=False)
    bisdelete = serializers.BooleanField(label='逻辑删除',required=False)

    ##关联相关对象 默认生成的关键字 heroinfo_set
    # heroinfo_set=serializers.PrimaryKeyRelatedField(label='关联英雄',read_only=True,many=True)
    # heroinfo_set = serializers.StringRelatedField(read_only=True, many=True) ##many=True得写


    ##允许自定义其他字段，或者不完全与原模型字段相同（可以少一些字段）
    bage=serializers.IntegerField(label='适合年龄',required=False)




    # ##追加校验方法,针对哪个字段校验就写哪个字段的名字  value是前端传入的单独字段数据
    # def validate_btitle(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError('there is not related to django')
    #     return value ##返回给attrs

    # ##对多个字段 进行联合校验
    # def validate(self, attrs):
    #     #attr是前端传入的所有字段数据
    #     bread=attrs['bread'] #提取bread字段的数据
    #     bcomment=attrs['bcomment'] #提取bcomment字段的数据
    #
    #     if bread<bcomment:
    #         raise serializers.ValidationError('the data is not real')
    #     return attrs ##返回给validated_data


    ##手动将将校验后的对象增加或更新,save（）方法
    ##固定方法，将校验后的数值，以键值对的形式传参给模型对象，并调用create方法，实现新增
    def create(self, validated_data):
        book=BookInfo.objects.create(**validated_data)
        return book  ##返回给save（）值


    ##固定方法，将带有instance即模型对象，和校验后的数据，一同传入，并调用update方法，更新模型
    def update(self, instance, validated_data):
        instance.id=validated_data['id']
        instance.btitle=validated_data['btitle']
        instance.bpubdate=validated_data['bpubdate']
        instance.save()
        return instance  ##返回给save（）值












class HeroInfoSerializer(serializers.Serializer):
    GENDER_CHOICES=(
        (0,'female'),
        (1,'male')
    )
    ##定义表单字段（属性）
    htitle = serializers.CharField(max_length=20, label='名称',read_only=True)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES,label='性别',required=False)
    hdiscribe = serializers.CharField(max_length=20, label='描述信息',required=False)
    ##PrimaryKeyRelatedField 输出主键id
    # hbook= serializers.PrimaryKeyRelatedField(label='与书籍关联',read_only=True)
    # ##StringRelatedField 输出主键对象中的__str__方法
    # hbook = serializers.StringRelatedField(label='与书籍关联', read_only=True)
    ##将关联对象的序列化器都显示出来
    # hbook = BookInfoSerializer()
    hisdelete = serializers.BooleanField(label='逻辑删除',required=False)











