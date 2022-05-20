from rest_framework import serializers
from .models import GlobalGallary, wait_for_address, wait_for_you
from django.contrib.auth import get_user_model
#from snippet import 

User = get_user_model()
class GlobalGallarySerializer(serializers.ModelSerializer):
    #title = serializers.CharField(required=True,source=GlobalGallary.item.title)
   # owner = serializers.CharField(required=True,source=GlobalGallary.item.user)
    
    #装饰器
    item_title = serializers.ReadOnlyField()
    item_owner = serializers.ReadOnlyField()
    item_img = serializers.ImageField(read_only=True)
    item_desc = serializers.ReadOnlyField()
    class Meta:
        model = GlobalGallary
        fields = "__all__"

class wait_for_address_serializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.ReadOnlyField()
    user_available = serializers.ReadOnlyField()
    def create(self,validated_data):
        in_queue = wait_for_address.objects.create(**validated_data)
        return in_queue
    class Meta:
        model = wait_for_address
        fields = "__all__"


class GlobalRankingSerializer(serializers.ModelSerializer):
    portrait_img = serializers.ImageField(read_only=True)
    class Meta:
        model = User
        fields = ["username","portrait_img","nation","sent_num"]


