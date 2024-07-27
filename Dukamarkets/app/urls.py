
from django.contrib import admin
from django.urls import path
from django.conf import settings #this code is written for images uploading from models
from django.conf.urls.static import static #this code is written for images uploading from models
from . import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('base/',views.Base,name='base'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #this code is written for images uploading from models
