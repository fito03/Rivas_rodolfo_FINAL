"""rivas_rodolfo_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app_FINAL import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('usuario/', views.usuario),

    path('instituciones_form/', views.instituciones_form),
    path('instituciones_list/', views.instituciones_list),
    path('instituciones_detalle/<int:id>/', views.instituciones_detalle),

    path('inscritos_form/', views.inscritos_form),
    path('inscritos_list/', views.Inscritos_List.as_view()),
    path('inscritos_detalle/<int:id>/', views.Inscritos_Detalle.as_view()),
]
