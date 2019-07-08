#-*-coding:utf-8-*-

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    """
    用户信息表
    """
    nickname = models.CharField(max_length=16,verbose_name="昵称",null=False,blank=False)
    phone = models.IntegerField(verbose_name="手机号码")
    email = models.EmailField(max_length=11,verbose_name="邮箱")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    avatar = models.ImageField(upload_to="users/",null=True,blank=True,verbose_name="用户头像")
    birthday = models.DateField(null=False,blank=False,verbose_name="出生日期")
    gender_choices = (
        (0,"男"),
        (1,"女"),
    )
    gender = models.SmallIntegerField(choices=gender_choices,verbose_name="性别")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

class Token(models.Model):
    """
    用户token信息表
    """
    token = models.CharField(max_length=64,verbose_name="token")
    user = models.OneToOneField(to=UserProfile,null=True,blank=True,verbose_name="用户")
