from django.db.models import signals
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
import datetime
from django.utils import timezone
from .models import RandomPeopleProcess


User = get_user_model()
@receiver(signals.post_save, sender = RandomPeopleProcess)
def create_process(sender,instance=None, created=False, **kwargs):
    if created:
        instance.expired_time = instance.choose_time + datetime.timedelta(days=20)
        starttime = datetime.datetime.strptime(instance.choose_time.strftime('%Y-%m-%d'),'%Y-%m-%d')  #将时间先格式化
 
        endtime = datetime.datetime.strptime(instance.expired_time.strftime('%Y-%m-%d'),'%Y-%m-%d')

        instance.remain_time = (endtime-starttime).days

        instance.save()