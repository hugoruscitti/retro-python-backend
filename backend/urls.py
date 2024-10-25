from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from app import views

ROOT = './static'


urlpatterns = [
    path('', views.home, name='home'),
    path('subir', csrf_exempt(views.subir), name='subir'),
    path('obtener/<hash>', views.obtener, name='obtener'),
    path('ejemplos', views.ejemplos, name='ejemplos'),
    path('admin/', admin.site.urls),
] + static("proyecto", document_root=ROOT)
