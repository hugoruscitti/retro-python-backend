from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from django.conf.urls.static import static
from rest_framework.authtoken import views
from app import views

ROOT = './static'


urlpatterns = [
    path('', views.home, name='home'),
    #path('proyecto/subir', csrf_exempt(subir), name='proyecto.subir'),
    #path('proyecto/obtener/<proyecto_id>', csrf_exempt(obtener), name='proyecto.obtener'),
    path('admin/', admin.site.urls),
] + static("proyecto", document_root=ROOT)
