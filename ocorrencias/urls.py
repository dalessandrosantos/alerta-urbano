from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportar, name='reportar'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('painel/', views.painel, name='painel'),
]
