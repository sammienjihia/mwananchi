from django.contrib import admin
from models import Insms, Outsms, Failedsms, Blacklistsms

# Register your models here.

admin.site.register(Insms)
admin.site.register(Outsms)
admin.site.register(Failedsms)
admin.site.register(Blacklistsms)

