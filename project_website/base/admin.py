from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.http import HttpRequest
from .models import *
from .custom_admin import my_admin_site 

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = 'Telenium Import Admin'


    
    
class fujitsuConnectionsAdmin(admin.ModelAdmin):
    list_display = ["Connection Name", "Service State", "Service Bandwidth Rate", "Connection Layer", "Service Direction", "Path Group Information List"]
    list_editable = ['Connection Name', 'Service State']
    def has_delete_permission(self, request, obj = None):
        return False


for name in MODEL_NAMES:

    my_admin_site.register(globals()[f"{name}RevHistory"])
    admin.site.register(globals()[f"{name}"])