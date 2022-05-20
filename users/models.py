from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
#from send_postcard.models import VerifyCode 

#from django.contrib.auth.models import User
# Create your models here.

#User = get_user_model()

class Portrait(models.Model):
    height = models.PositiveSmallIntegerField(default=80)
    width = models.PositiveSmallIntegerField(default=80)
    image = models.ImageField(upload_to='protraits/',height_field='height',width_field='width')


NATIONALITY_CHOICES = (
        ('CN','中国'),
        ('FR','法国'),
        ('US','美国'),
        ('RU','俄罗斯'),
        ('JP','日本'), 
        )

'''
class User(models.Model):
    usrname = models.CharField(max_length=20,unique=True)
    regdate = models.DateTimeField('Date registered',auto_now_add=True)
    pw = models.CharField('password',max_length=25)
    realname = models.CharField(max_length=20)
    sex = models.CharField(max_length=1,choices=[[None,'请选择性别'],['M','男'],['F','女']])
    intro = models.TextField('自我介绍',blank=True)
    portrait = models.OneToOneField(Portrait,on_delete=models.CASCADE)
    nation = models.CharField(max_length=2,choices=NATIONALITY_CHOICES)
    add = models.TextField('收件地址')
    birth = models.DateField()
    class Meta:
        unique_together = ("id","usrname")
    
    def verify_password(self, password):
        return self.pw == password
    
    def __str__(self):
        return self.usrname

'''

class UserInfo(AbstractUser):
    birth = models.DateField(null=True)
    sex = models.CharField(max_length=1,choices=[[None,'请选择性别'],['M','男'],['F','女']],default='F')
    regdate = models.DateTimeField('Date registered',auto_now_add=True)
    nation = models.CharField(max_length=2,choices=NATIONALITY_CHOICES,default='CN')
    intro = models.TextField('自我介绍',blank=True,null=True)
    portrait = models.OneToOneField(Portrait,on_delete=models.CASCADE,null=True)
    add = models.TextField('收件地址',default='')
    
    
    process_related_num = models.PositiveIntegerField(default=0) # recevong + sending
    #如果在等待地址队列，或者 等待被发送地址队列，则不开启process （related_num不改变）
    #可添加判断队列是否为空，以避免程序无意义操作
    available_requiring_num = models.PositiveIntegerField(default=5) # 作为sender  5 - sending
    receving_num = models.PositiveIntegerField(default=0) # 
    #一个用户最多可以获取5个地址， 每当自己寄出去的明信片在20天内被对方确认收到，则视为
    sending_num = models.PositiveIntegerField(default=0)
    sent_num = models.PositiveIntegerField(default=0)
    tmp_message = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = "用户信息"
        
        unique_together = ("id","username")
    def __str__(self):
        return self.username
    @property
    def portrait_img(self):
        return self.portrait.image

class UserGallary(models.Model):
    #from send_postcard.models import VerifyCode 
    
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    own_image = models.ImageField(upload_to='postcards/',null=True,blank=True)
    
    code = models.ForeignKey('send_postcard.VerifyCode',default='',on_delete=models.CASCADE)
    title = models.CharField(max_length=20,blank=True,null=True)
    desc = models.TextField('说说这张明信片对你的意义吧',blank=True)  

    class Meta:
        verbose_name_plural = 'UserGallaries'
    def __str__(self):
        return self.title

    @property
    def get_username(self):
        return self.user.username
    