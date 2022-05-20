from django.shortcuts import render

from broad.models import wait_for_address, wait_for_you
from .models import VerifyCode, RandomPeopleProcess
import random
import string
import math
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from broad.serializers import wait_for_address_serializer
from .serializers import VerifyCodeSerializer, CreateProcessSerializer,RepoSerializer
from users.serializers import ReceiverStatsializer, UserStatsSerializer
from django.db.models import Min
from django.db import connection
# Create your views here.
User = get_user_model()


class send_available_view(APIView):
    
    def post(self,request):
        current_user = request.user
        
        if current_user.available_requiring_num > 0 :
            if wait_for_you.objects.count() > 0: #有人可以收到地址
                if wait_for_address.objects.count() > 0  and wait_for_address.objects.get(user=current_user):
                    print("yeah")
                    wait_for_address.objects.get(user=current_user).delete()
                index = wait_for_you.objects.all().aggregate(Min("id"))['id__min']
                receiver = wait_for_you.objects.get(id=index).user
                if current_user == receiver:
                    return Response("baam")
                current_user.available_requiring_num -= 1
                current_user.process_related_num += 1
                current_user.sending_num += 1
                receiver.receving_num += 1
                receiver.process_related_num += 1
                current_user.save()
                receiver.save()
                if wait_for_address.objects.count() == 0:
                    with connection.cursor() as c:
                        c.execute("alter table broad_wait_for_address auto_increment = 1;")
                    #queue = wait_for_address(user=current_user,id=1) 
               
                
                
                '''
                生成唯一的编码
                '''
                
                confirm_code = current_user.nation + '-' +  ''.join(random.sample(string.ascii_uppercase+ string.digits,6))
                wait_for_you.objects.get(id=index).delete()
                new_code = VerifyCode(sender=current_user,receiver=receiver,code=confirm_code) #创建一个标识码
                new_code_ser = VerifyCodeSerializer(new_code)#序列化标识码，返回给前端
                new_code.save()
                receiver_ser = ReceiverStatsializer(receiver) #序列化地址，返回给前端

                '''
                生成一条process

                '''
                new_process = RandomPeopleProcess(sender=current_user,receiver=receiver,code=new_code,status="sending")
                new_process.save()
                new_process_ser = CreateProcessSerializer(new_process)

                
                user_stats_ser = UserStatsSerializer(current_user)
                
                final_res = {**new_code_ser.data,**receiver_ser.data,**new_process_ser.data,**user_stats_ser.data}
                #final_res.update({'availiable_num':current_user.available_requiring_num})
                return Response(final_res)
            else:                            #没人可以收到地址
                with connection.cursor() as c:
                    c.execute("alter table broad_wait_for_you auto_increment = 1;")
                if wait_for_address.objects.count() == 0 or wait_for_address.objects.get(user=current_user) == False:

                    queue = wait_for_address(user=current_user)#生成一条  z入队列
                    res = wait_for_address_serializer(queue)  #加入队列
                    queue.save()
                return Response("Please come back later")
                
        else:
            return Response("you can get at most 5 addresses")


class repo_view(APIView):
    def post(self,request):
        
        repo = RepoSerializer(data=request.data)
        
        if repo.is_valid() and RandomPeopleProcess.objects.get(code__code=request.data['confirm_code']):
            
            process = RandomPeopleProcess.objects.get(code__code=request.data['confirm_code'])
            
            process.status = 'success'
            process.sender.sending_num -= 1
            process.sender.process_related_num -= 1
            process.sender.sent_num += 1
            process.sender.tmp_message = True #这里我是接收的我是接收的！！
            request.user.process_related_num -= 1
            request.user.receving_num -= 1
            wait_for_you(user=process.sender)
            UserGallary(user=request.user,code=VerifyCode.objects.get(code=request.data['confirm_code']), desc="my reply: "+request.data['reply'])
            call = "his" if request.sex == "M" else "her"
            UserGallary(user=process.sender,code=VerifyCode.objects.get(code=request.data['confirm_code']), desc=(call + " reply: "+request.data['reply']))
            return Response(repo.data)
        return Response(repo.errors)
        
        

        
    

