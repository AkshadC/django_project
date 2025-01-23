
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from base import views as base_views
from base.custom_admin import my_admin_site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/', my_admin_site.urls), 
    path('', include('base.urls')),
    path('auto-login/', base_views.auto_login, name='auto_login'),

]
