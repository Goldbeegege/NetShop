#—*-coding:utf-8-*-


from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

user = get_user_model()
# Create your models here.


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(to=user,verbose_name="购物车所属用户")
    goods = models.ForeignKey(to=Goods,verbose_name="购物车中的货物")
    num = models.IntegerField(default=0,verbose_name="数量")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        unique_together = ("user","goods")

    def __str__(self):
        return self.user


class OrderInfo(models.Model):
    """
    订单信息
    """
    user = models.ForeignKey(to=user,verbose_name="订单所属用户")
    order_sn = models.CharField(max_length=128,blank=True,null=True,unique=True,verbose_name="订单号")
    trade_no = models.CharField(max_length=128,blank=True,null=True,unique=True, verbose_name="交易号")
    status_choices = (
        (0,"交易成功"),
        (1,"交易超时"),
        (2,"创建交易"),
        (3,"交易结束"),
        (4,"待支付"),
    )
    pay_status = models.SmallIntegerField(choices=status_choices,default=4,verbose_name="交易状态")
    message = models.CharField(max_length=256,verbose_name="订单留言")
    order_amount = models.FloatField(default=0.0,verbose_name="订单金额")
    pay_time = models.DateTimeField(blank=True,null=True,verbose_name="支付时间")

    #收获信息
    address = models.CharField(max_length=200, default="", verbose_name="收货地址")
    picker_name = models.CharField(max_length=32, default="", verbose_name="收货人姓名")
    picker_phone = models.IntegerField(default="", verbose_name="收货人电话")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


class OrderGoods(models.Model):
    """
    订单商品详情表
    """
    order = models.ForeignKey(to=OrderInfo,verbose_name="订单")
    goods = models.ForeignKey(to=Goods,verbose_name="商品")
    goods_num = models.IntegerField(verbose_name="商品数量",default=0)

    class Meta:
        verbose_name = "订单商品详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order