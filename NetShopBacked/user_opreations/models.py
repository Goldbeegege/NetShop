#-*-coding:utf-8-*-

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

user = get_user_model()
# Create your models here.


class UserFav(models.Model):
    """
    用户收藏列表
    """
    user = models.ForeignKey(to=user,verbose_name="用户")
    goods = models.ForeignKey(to=Goods,verbose_name="商品")

    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")


    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user

class UserLeavingMsg(models.Model):
    """
    用户留言
    """
    user = models.ForeignKey(to=user,verbose_name="用户")
    type_choices = (
        (0, "留言"),
        (1, "投诉"),
        (2, "询问"),
        (3, "售后"),
        (4, "求购")
    )
    msg_type = models.SmallIntegerField(default=0,verbose_name="留言类型")
    subject = models.CharField(max_length=100,default="",verbose_name="留言主题")
    content = models.TextField(default="",verbose_name="留言内容")
    file = models.FileField(upload_to="leavingmsg/images/",verbose_name="上传文件")


    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject

class UserAddress(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(to=user,verbose_name="用户")
    province = models.CharField(max_length=64,verbose_name="省份",default="")
    city = models.CharField(max_length=64,default="",verbose_name="市")
    district = models.CharField(max_length=128,default="",verbose_name="区域")
    address_info = models.CharField(max_length=256,default="",verbose_name="详细信息")

    class Meta:
        verbose_name = "用户收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user
