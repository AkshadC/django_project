# custom_admin.py
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Table Histories'
    site_title = 'Admin Portal'
    index_title = 'Table Revision Histories'

my_admin_site = MyAdminSite(name='myadmin')
