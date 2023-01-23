"""myproject URL Configuration

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
from django.urls import path, re_path
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime

from app import views as main_views
from additem import views as additem_views
from viewPurchaseOrder import views as viewPo_views
from arPurchaseOrder import views as arviewPo_views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^contact$', main_views.contact, name='contact'),
    re_path(r'^about$', main_views.about, name='about'),
    re_path(r'^login/$',
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/index.html'),
        name='logout'),
    re_path(r'^menu$', main_views.menu, name='menu'),
    re_path(r'^additemform$', additem_views.additemform, name='additem_form'),
    re_path(r'^additemconfirmation$', additem_views.additemconfirmation, name='additem_confirmation'),
    
    re_path(r'^viewPo/$', viewPo_views.viewPo, name='viewPo'),
    re_path(r'^viewPo/searchPo$', viewPo_views.searchPo, name='searchPo'),
    re_path(r'^viewPo/selectPo$', viewPo_views.selectPo, name='selectPo'),
    re_path(r'^backtoHome$', viewPo_views.backtoHome, name='backtoHome'),
    re_path(r'^viewPo/backtoHome$', viewPo_views.backtoHome, name='backtoHome'),
    re_path(r'^viewPo/backtoList$', viewPo_views.backtoList, name='backtoList'),
    re_path(r'^viewPo/approvePo$', viewPo_views.approvePo, name='approvePo'),
    re_path(r'^viewPo/rejectPo$', viewPo_views.rejectPo, name='rejectPo'),

    re_path(r'^arviewPo$', arviewPo_views.arviewPo, name='arviewPo'),
    re_path(r'^arviewPo/$', arviewPo_views.arviewPo, name='arviewPo'),
    re_path(r'^arviewPo/arsearchPo$', arviewPo_views.arsearchPo, name='arsearchPo'),
    re_path(r'^arviewPo/arselectPo$', arviewPo_views.arselectPo, name='arselectPo'),
    re_path(r'^arviewPo/arbacktoHome$', arviewPo_views.arbacktoHome, name='arbacktoHome'),
    re_path(r'^arviewPo/arbacktoList$', arviewPo_views.arbacktoList, name='arbacktoList'),
    re_path(r'^arviewPo/arapprovePo$', arviewPo_views.arrejectPo, name='arrejectPo'),
    re_path(r'^arviewPo/arrejectPo$', arviewPo_views.arrejectPo, name='arrejectPo'),
    re_path(r'^arselectPo$', arviewPo_views.arselectPo, name='arselectPo'),
    re_path(r'^arsearchPo$', arviewPo_views.arsearchPo, name='arsearchPo'),
    re_path(r'^arbacktoHome$', arviewPo_views.arbacktoHome, name='arbacktoHome'),
    re_path(r'^arbacktoList$', arviewPo_views.arbacktoList, name='arbacktoList'),
    re_path(r'^arapprovePo$', arviewPo_views.arapprovePo, name='arapprovePo'),
    re_path(r'^arrejectPo$', arviewPo_views.arrejectPo, name='arrejectPo'),
]