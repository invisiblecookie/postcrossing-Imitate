from django.shortcuts import render
from django.views import View

#from django.http import JsonResponse, HttpResponse
from .models import GlobalGallary
from users.models import UserGallary
#from django.forms.models import model_to_dict
#from snippets.serializers import SnippetSerializer
from .serializers import GlobalGallarySerializer,GlobalRankingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import threading
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "broad/index.html", {})

class GlobalGallaryView(APIView):

    
        
    
    def get(self,request,format=None):
        cards = GlobalGallary.objects.all()
        GlobalGallary_serializer = GlobalGallarySerializer(cards,many=True)
        print(request.user)
        return Response(GlobalGallary_serializer.data)

    
class GlobalRankingView(APIView):
    def get(self,request):
        queryset = User.objects.order_by("sent_num")[:3]
        #print(queryset)
        GlobalRanking_serializer = GlobalRankingSerializer(queryset,many=True)
        return Response(GlobalRanking_serializer.data)
    def post(self,request):
        
        queryset = User.objects.filter(nation=request.data['country']).order_by("sent_num")[:3]
        CountryRanking_serializer = GlobalRankingSerializer(queryset,many=True)
        return Response(CountryRanking_serializer.data)

'''

class GlobalGallaryView(View):
    def get(self,request):
        json_list = []
        cards = GlobalGallary.objects.all()
        
        for card in cards:
            json_dict = {}
            json_dict["title"] = card.item.title
            #json_dict["img"] = card.item.own_image
            json_dict["owner"] = card.item.user.username
            json_dict["desc"] = card.item.desc
            json_list.append(json_dict)
        
        for card in cards:
            items = card.item.objects,all()
            for item in items:

                json_dict = model_to_dict(item)
                json_list.append(json_dict) 
        

        from django.core import serializers
        for card in cards:
            
            item_name = card.item.title
            data = UserGallary.objects.get(title=item_name)
            json_list.append(data)
        json_data = serializers.serialize("json",json_list)
        json_data = json.loads(json_data)
        return HttpResponse(json.dumps(json_data), content_type="application/json")


'''


