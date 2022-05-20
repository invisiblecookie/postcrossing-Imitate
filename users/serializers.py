from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import UserGallary
from rest_framework.validators import UniqueValidator


User = get_user_model()
class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all(),message="username is existed")])
    password = serializers.CharField(style={'input_type': 'password'})

    def create(self,validated_data):
        user = super(UserRegSerializer,self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("username","email","password","sex","intro","add")

class ReceiverStatsializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["add","nation","intro","sex"]


class UserStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["process_related_num", "available_requiring_num","receving_num","sending_num","sent_num"]



class UserProfileSerializer(serializers.ModelSerializer):
    portrait_img = serializers.ImageField(read_only=True)
    class Meta:
        model = User
        fields = "__all__"