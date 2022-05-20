from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
#from users.models import Profile
from django.contrib.auth import get_user_model
import random
import string
import math

# Create your models here.

User = get_user_model()



class VerifyCode(models.Model):
    sender = models.ForeignKey(User,related_name="c_sender",on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name="c_receiver",on_delete=models.CASCADE)
    #confirm_code = Profile.nation + '-' +  ''.join(random.sample(string.ascii_uppercase+ string.digits,6))
    code = models.CharField(max_length=9,unique=True)
    starttime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class RandomPeopleProcess(models.Model):
    STATUS_CHOICES = (
        ('success','成功到达'),
        ('sending','正在路上'),
        ('expired','已过期')
    )
    
    sender = models.ForeignKey(User,related_name="p_sender",on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name="p_receiver",on_delete=models.CASCADE)
    choose_time = models.DateTimeField(auto_now_add=True)
    code = models.OneToOneField(VerifyCode,on_delete=models.CASCADE,default='')
    status = models.CharField('状态',choices=STATUS_CHOICES,max_length=10) 
    expired_time = models.DateTimeField(null=True)
    #剩余时间 按分钟计算 20天的锁定日期
    remain_time = models.IntegerField(null=True)    # math.floor()
    

    class Meta:
        verbose_name_plural = 'RandomPPlProcesses'

    @property
    def sender_name(self):
        return self.sender.username
    @property
    def receiver_name(self):
        return self.receiver.username


