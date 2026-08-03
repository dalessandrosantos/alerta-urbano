from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportar, name='reportar')
]
