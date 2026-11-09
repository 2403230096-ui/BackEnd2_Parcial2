from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_autos, name='lista_autos'),
    path('agregar/', views.agregar_auto, name='agregar_auto'),
]