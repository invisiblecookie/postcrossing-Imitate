
#import json
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import UserRegSerializer, UserProfileSerializer
from django.db import connection
import threading
from django.contrib.auth import authenticate
import pymysql
# Create your views here.


User = get_user_model()


class MyBackend(ModelBackend):
    """
    def get_my_message(self,username):
        
        with connection.cursor() as fc:
            trigger = '''delimiter $$
drop trigger if exists find_message$$
create trigger find_message
after insert on  users_usergallary for each row  
begin
if new.user_id = (select * from users_userinfo where username='{0}') and (new.desc like 'his reply:%'or new.desc like 'her reply:%')
then 
update users_userinfo set tmp_message = False  where username='{0}'; 
end if;
end$$
delimiter ;'''.format(username)
            
            #fc.execute("drop trigger if exists find_message;")
            fc.execute(trigger,[username])
        current_user = User.objects.get(username=username)
        if current_user.tmp_message == False:
            print("replied")
            return HttpResponse("you have receieved a reply, please check your gallary")
"""


    def authenticate(self,request,username=None,password=None):
        #login = (settings.ADMIN_LOGIN == username)
        #pwd = check_password(password,settings.ADMIN_PASSWORD)
        print("start")
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            print(user)
            if user.check_password(password):
                print("goto thread")
                #t = threading.Thread(target=self.get_my_message,args=(username,))
                #t.setDaemon(True)
                #t.start()
                return user
        except Exception as e:
            print("excep")
            return None
    

class UserViewset(CreateModelMixin,UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = UserRegSerializer
    queryset = User.objects.all()


class UserProfileView(APIView):
    def get(self,request,username):
        user = User.objects.get(username=username)
        you = UserProfileSerializer(user)
        return Response(you.data)




            
            


'''
class RegisterView(View):
    def get(self,request):
        set = models.User.objects.values('usrname')
        return JsonResponse({
                "code": 0,
                "data": list(set)
                })
    def post(self,request):
        if request.method == "POST":
            user_form=UserRegisterationForm(json.loads(request.body.decode()))
            if user_form.is_valid():
                new_user=user_form.save()
                #instance = new_user.save()
                return JsonResponse({
                        "code": 0,
                        "data": new_user
                        })
            else:
                return JsonResponse({
                        "code": 1,
                        "data": user_form.errors
                        })
        else:
            user_form=UserRegisterationForm()
        



'''

'''
class LoginView(View):
    def get(self,request):
        
    
    
    def post(self,request):
        if request.method == "POST":
'''   


'''
def loginView():
      if request.method == 'POST':

        form=LoginForm(request.POST)

        if form.is_valid():

            cd=form.cleaned_data

'''