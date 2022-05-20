from django.db import models
from django.utils import timezone
from users.models import UserInfo
from users.models import UserGallary
# Create your models here.

'''
两个队列
'''

class wait_for_address(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "等待收到新地址队列" 
        verbose_name_plural = verbose_name
        ordering = ['add_time']
    @property
    def username(self):
        return self.user.username
    @property
    def user_available(self):
        return self.user.available_requiring_num

class wait_for_you(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "等待有人收到你的地址队列"
        verbose_name_plural = verbose_name
        ordering = ['add_time'] 

class GlobalGallary(models.Model):
    item = models.OneToOneField(UserGallary,on_delete=models.CASCADE,related_name="g_item")
    '''
    title =  models.OneToOneField(UserGallary,to_field="title",on_delete=models.CASCADE,related_name="g_title")
    img =  models.OneToOneField(UserGallary,to_field="own_image",on_delete=models.CASCADE,related_name="g_img",null=True)
    owner =  models.OneToOneField(UserGallary,to_field="user",on_delete=models.CASCADE,related_name="g_owner")
    desc =  models.OneToOneField(UserGallary,to_field="desc",on_delete=models.CASCADE,related_name="g_desc")
    '''
    class Meta:
        verbose_name_plural = 'GlobalGallaries'


    @property
    def item_title(self):
        return self.item.title
    @property
    def item_owner(self):
        return self.item.get_username
    @property
    def item_img(self):
        return self.item.own_image
    @property
    def item_desc(self):
        return self.item.desc