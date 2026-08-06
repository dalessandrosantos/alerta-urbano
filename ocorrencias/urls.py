from django.contrib.auth import views as auth_views # Login e logout prontos
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportar, name='reportar'),
    path('painel/', views.painel, name='painel'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('deletar/<int:pk>/', views.deletar, name='deletar'),
    path('login/', auth_views.LoginView.as_view(), name='login')
]
