#-*-coding:utf-8-*-

from django.db import models

# Create your models here.

class GoodsCategory(models.Model):
    """"
    商品分类表
    """
    name = models.CharField(max_length=32,null=True,blank=True,verbose_name="商品类别",help_text="商品类别")
    code = models.CharField(max_length=32,verbose_name="商品code",null=True,blank=True,help_text="商品code")
    desc = models.TextField(default="",verbose_name="类别描述",help_text="类别描述")
    category_choices = (
        (0,"一级类别"),
        (1,"二级类别"),
        (2,"三级类别"),
    )

    category_type = models.SmallIntegerField(choices=category_choices,default=0)
    parent_type = models.ForeignKey(to="self",null=True,blank=True,related_name="sub_category",verbose_name="父级类别")
    is_tab = models.BooleanField(default=False,verbose_name="是否有导航栏")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class GoodsBrand(models.Model):
    """
    商品品牌表
    """
    catatory = models.ForeignKey(to=GoodsCategory,related_name="brand",verbose_name="品牌类别")
    name = models.CharField(max_length=32,verbose_name="商品名")
    desc = models.TextField(default="",verbose_name="品牌描述信息")
    img = models.ImageField(upload_to="brands/",verbose_name="品牌头像")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")


    class Meta:
        verbose_name = "商品品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=128,null=False,blank=False,verbose_name="商品名")
    category = models.ForeignKey(to=GoodsCategory,null=False,blank=False,verbose_name="商品所属类别",related_name="goods")
    brand = models.ForeignKey(to=GoodsBrand,null=True,blank=True,verbose_name="商品所属品牌",related_name="goods_to_brand")
    goods_sn = models.CharField(max_length=64,default="",verbose_name="商品唯一货号")
    click_num = models.IntegerField(default=0,verbose_name="点击数")
    sold_num = models.IntegerField(default=0,verbose_name="销售数")
    fav_num = models.IntegerField(default=0,verbose_name="收藏数")
    goods_num = models.IntegerField(default=0,verbose_name="库存数")
    market_price = models.FloatField(default="",verbose_name="市场价")
    shop_price = models.FloatField(default="",verbose_name="本店价格")
    goods_brief = models.TextField(default="",verbose_name="商品简介")
    desc = models.TextField(default="",verbose_name="描述内容")
    delivery_fee = models.FloatField(default=0.0,verbose_name="运费")
    is_new = models.BooleanField(default=False,verbose_name="是否为新品")
    is_hot = models.BooleanField(default=False,verbose_name="是否热销")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")


    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category',verbose_name="商品类目")
    goods =models.ForeignKey(Goods, related_name='goods')

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods

class Slide(models.Model):
    goods = models.ForeignKey(to=Goods,related_name="images",verbose_name="商品")
    image = models.ImageField(upload_to="",null=True,blank=True,verbose_name="图片")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods

class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords

