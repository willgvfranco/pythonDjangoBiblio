"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('neuadmin/', admin.site.urls),
    path('relatorio/', include('relatorio.urls')),
    path('crud/', include('crud.urls')),
    path('paginacao/', include('paginacao.urls')),
    path('facedjango/', include('facedjango.urls')),
    path('fusion/', include('fusion.urls')),

]

admin.AdminSite.site_header = "Sistema XYZ"
admin.AdminSite.site_title = "Geek University"
admin.AdminSite.index_title = "Meu sistema super legal"
