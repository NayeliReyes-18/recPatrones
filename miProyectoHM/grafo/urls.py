from django.urls import path, re_path
from .views import grafo,procesaGrafo
from . import views

#app_name = 'grafo'

urlpatterns = [
    path('grafo/',grafo,name="grafo"),
    path('procesaGrafo',procesaGrafo,name="procesaGrafo")
]