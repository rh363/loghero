"""
URL configuration for sample_project project.

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
from django.shortcuts import redirect
from django.urls import path
from api.views import index

def go_to_admin(request):
    return redirect('admin/')

admin.site.site_url = '/api/'
admin.site.site_header = 'Test Loghero'
admin.site.site_title = 'Test Loghero'
admin.site.index_title = 'Test Loghero'

urlpatterns = [
    path('', go_to_admin),
    path('admin/', admin.site.urls),
    path('api/', index)
]
