"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
#from users import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from mysite.settings import MEDIA_ROOT
#import xadmin
from rest_framework.authtoken import views
from broad.views import GlobalGallaryView,GlobalRankingView,FrontendRenderView
#from django.contrib.staticfiles.views import serve
#from users.views import login
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from users.views import UserViewset,MyBackend,UserProfileView
from send_postcard.views import send_available_view, repo_view
router = DefaultRouter()
router.register('users',UserViewset,base_name = "users")
#router.register('send',send_available_viewset,base_name="send_request")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('xadmin/',xadmin.site.urls),
    #path('login/', views.LoginView, name='login')
    #path('registeration/',views.RegisterView.as_view(), name='registeration'),
    
#]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    re_path(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}) ,

    path('globalgallary/',GlobalGallaryView.as_view(),name="globalgallary"),
    path('api-token-auth/',views.obtain_auth_token),
    path('login/',obtain_jwt_token),
    path('',include(router.urls)),
    path('send_request/',send_available_view.as_view(),name="send_request"),
    path('repo/',repo_view.as_view(),name="repo"),
    path('globalranking/',GlobalRankingView.as_view(),name="ranking"),
    path('globalranking/countries/',GlobalRankingView.as_view(),name="country_order"),
    path('user/<str:username>/',UserProfileView.as_view(),name="profile")
    #path('countries/',)
    ]

urlpatterns += [
        re_path(r'(?P<path>.*)',FrontendRenderView.as_view(),name='home')
    ]
