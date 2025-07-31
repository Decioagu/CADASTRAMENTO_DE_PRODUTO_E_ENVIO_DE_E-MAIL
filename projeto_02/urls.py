"""
URL configuration for projeto_02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static #11
from django.conf import settings #11

from core.views import index, contato, produto #10 Importando as views do core (app)

urlpatterns = [
    path('admin/', admin.site.urls), #10 Rota para o Django Admin
    path('', index, name='index'),  #10 Rota para a página inicial
    path('contato/', contato, name='contato'),  #10 Rota para a página de contato
    path('produto/', produto, name='produto'),  #10 Rota para a página de produto/id
]
#11 Verifica se o modo DEBUG está ativado
if settings.DEBUG:  
    #11 Adiciona as URLs de mídia ao urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 