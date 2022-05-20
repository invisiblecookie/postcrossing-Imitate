import xadmin
from .models import  UserGallary, Portrait


'''
class UserInfoAdmin(object):
    pass
xadmin.site.register(UserInfo, UserInfoAdmin)
'''
class PortraitAdmin(object):
    pass
class UserGallaryAdmin(object):
    pass


xadmin.site.register(UserGallary,UserGallaryAdmin)
xadmin.site.register(Portrait,PortraitAdmin)