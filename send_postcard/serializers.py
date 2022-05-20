from rest_framework import serializers
from .models import VerifyCode, RandomPeopleProcess
import re

class VerifyCodeSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = VerifyCode
        fields = ["code"]


class CreateProcessSerializer(serializers.ModelSerializer):
    sender_name = serializers.ReadOnlyField()
    receiver_name = serializers.ReadOnlyField()
    class Meta:
        model = RandomPeopleProcess
        fields = ["choose_time","expired_time","remain_time","sender_name","receiver_name"]


class RepoSerializer(serializers.Serializer):
    confirm_code = serializers.CharField(min_length=9,max_length=9)
    def validate_confirm_code(self,confirm_code):
        #confirm_code = current_user.nation + '-' +  ''.join(random.sample(string.ascii_uppercase+ string.digits,6))
        '''
        用正则验证, code规则如上
        '''

        confirm_code_regex = re.compile(r'[A-Z]{2}-[A-Z0-9]{6}')
        if not confirm_code_regex.match(confirm_code):
            raise serializers.ValidationError("请输入正确的标识码")
        return confirm_code
    reply = serializers.CharField(max_length=140)
    