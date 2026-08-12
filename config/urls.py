"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Importa as configurações do projeto (settings.py)
from django.conf import settings

# Importa a função para servir arquivos estáticos e de mídia no ambiente de desenvolvimento
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ocorrencias.urls'))
]

# Se o projeto estiver em modo de desenvolvimento (DEBUG = True)
if settings.DEBUG:
    # Adiciona a rota para carregar as imagens/arquivos de mídia no navegador durante os testes
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)