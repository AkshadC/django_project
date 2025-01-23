from django.urls import path
from . import views
from .views import upload_excel
urlpatterns = [
    path('', views.index, name='index'),
    path('add-site-data/', views.add_site_data, name='add_site_data'),
    path('upload-excel/', upload_excel, name='upload_excel'),

]