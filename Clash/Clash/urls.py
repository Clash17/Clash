"""Clash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from round1 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='0'),
    url(r'^signup', views.signup, name='7'),
    url(r'^login', views.login_page, name='1'),
    url(r'^check', views.check, name='2'),
    url(r'^question', views.question, name='2'),
    url(r'^ans', views.ans, name='2'),
    url(r'^submit', views.eval, name='2'),
    url(r'^harmonic', views.harmonic, name='2'),
    url(r'^delete', views.delete, name='2'),
    url(r'^logout', views.logoutfunc, name='2'),

]
