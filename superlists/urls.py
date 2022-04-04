"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url

from lists.views import home_page, view_list, new_list, add_item

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^lists/(\d+)/$', view_list, name='view_list'),
    url(r'^lists/(\d+)/add_item$', add_item, name='add_item'),
    url(r'^lists/new$', new_list, name='new_list'),
]
