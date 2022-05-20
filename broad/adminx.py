import xadmin
from .models import wait_for_address, wait_for_you

class wait_for_addressAdmin(object):
    pass

class wait_for_youAdmin(object):
    pass

xadmin.site.register(wait_for_address,wait_for_addressAdmin)
xadmin.site.register(wait_for_you,wait_for_youAdmin)