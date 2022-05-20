from django.contrib import admin
from users.models import Portrait,UserInfo, UserGallary

# Register your models here.

#admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(Portrait)
admin.site.register(UserGallary)