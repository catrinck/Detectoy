"""
URL configuration for detectoyBackEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Detectoy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gerentes/', views.gerentes),
    path('api/gerentes/<int:cpf>', views.gerentes_modificar),
    path('api/funcionarios/', views.funcionarios),
    path('api/funcionarios/<int:cpf>', views.funcionarios_modificar),
    path('api/login/gerentes/', views.gerente_login),
    path('api/login/funcionarios/', views.funcionario_login),
]
