import xadmin
from .models import VerifyCode, RandomPeopleProcess




class VerifyCodeAdmin(object):
    pass
class RandomPeopleProcessAdmin(object):
    def has_delete_permission(self):
        return True

xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(RandomPeopleProcess, RandomPeopleProcessAdmin)