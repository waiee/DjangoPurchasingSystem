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
from submitQuotation import views as subQuo_views
from submitQuotation import views as quoList_views
from submitQuotation import views as quoDetail_views
from viewquotation import views as viewquo_views
from arQuotation import views as arviewquo_views
from createPurchaseOrder import views as createPurchaseOrder_views
from viewPurchaseOrderStatus import views as viewPurchaseOrderStatus_views
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
    
    #Purchaser
    re_path(r'^submitQuotation$', subQuo_views.submitQuotation, name='submit_quotation'),
    re_path(r'^quotationConfirm$', subQuo_views.quotationConfirmation, name='quotation_confirmation'),
    re_path(r'^addQuotationItem$', subQuo_views.addQuotationItem, name='add_quotation_item'),
    re_path(r'^QuotationItemList$', subQuo_views.QuotationItemList, name='quotation_item_list'),
    re_path(r'^quotationList$', quoList_views.quotationList, name='quotation_list'),
    re_path(r'^quotationDetail$', quoDetail_views.quotationDetail, name='quotation_detail'),

    #Employee
    re_path(r'^viewquo', viewquo_views.viewquo, name='viewquo'),
    re_path(r'^viewquo/', viewquo_views.viewquo, name='viewquo'),
    re_path(r'^viewquo/selectquo$', viewquo_views.selectquo, name='selectquo'),
    re_path(r'^selectquo$', viewquo_views.selectquo, name='selectquo'),
    re_path(r'^viewquo/backtoHome$', viewquo_views.backtoHome, name='backtoHome'),
    re_path(r'^viewquo/backtoHome/$', viewquo_views.backtoHome, name='backtoHome'),
    re_path(r'^backtoHome$', viewquo_views.backtoHome, name='backtoHome'),
    re_path(r'^viewquo/approvequo$', viewquo_views.approvequo, name='approvequo'),
    re_path(r'^approvequo$', viewquo_views.approvequo, name='approvequo'),
    re_path(r'^viewquo/rejectquo$', viewquo_views.rejectquo, name='rejectquo'),
    re_path(r'^rejectquo$', viewquo_views.rejectquo, name='rejectquo'),
    re_path(r'^backtoList$', viewquo_views.backtoList, name='backtoList'),
    re_path(r'^viewquo/backtoList$', viewquo_views.backtoList, name='backtoList'),
    re_path(r'^searchquo$', viewquo_views.searchquo, name='searchquo'),
    re_path(r'^viewquo/searchquo$', viewquo_views.searchquo, name='searchquo'),

    re_path(r'^arviewquo', arviewquo_views.arviewquo, name='arviewquo'),
    re_path(r'^arviewquo/', arviewquo_views.arviewquo, name='arviewquo'),
    re_path(r'^arviewquo/selectquo$', arviewquo_views.arselectquo, name='arselectquo'),
    re_path(r'^arselectquo$', arviewquo_views.arselectquo, name='arselectquo'),
    re_path(r'^arviewquo/arbacktoHome$', arviewquo_views.arbacktoHome, name='arbacktoHome'),
    re_path(r'^arbacktoHome$', arviewquo_views.arbacktoHome, name='arbacktoHome'),
    re_path(r'^arviewquo/arapprovequo$', arviewquo_views.arapprovequo, name='arapprovequo'),
    re_path(r'^arapprovequo$', arviewquo_views.arapprovequo, name='arapprovequo'),
    re_path(r'^arviewquo/arrejectquo$', arviewquo_views.arrejectquo, name='arrejectquo'),
    re_path(r'^arrejectquo$', arviewquo_views.arrejectquo, name='arrejectquo'),
    re_path(r'^arbacktoList$', arviewquo_views.arbacktoList, name='arbacktoList'),
    re_path(r'^arviewquo/arbacktoList$', arviewquo_views.arbacktoList, name='arbacktoList'),
    re_path(r'^arsearchquo$', arviewquo_views.arsearchquo, name='arsearchquo'),
    re_path(r'^arviewquo/arsearchquo$', arviewquo_views.arsearchquo, name='arsearchquo'),

    #Finance Officer
    re_path(r'^createPurchaseOrder$', createPurchaseOrder_views.createPurchaseOrder, name='createPurchaseOrder'),
    re_path(r'^quotationList$', createPurchaseOrder_views.quotationList, name='quotationList'),
    re_path(r'^quotationDetail$', createPurchaseOrder_views.quotationDetail, name='quotationDetail'),
    re_path(r'^purchaseOrderDetail$', createPurchaseOrder_views.purchaseOrderDetail, name='purchaseOrderDetail'),
    re_path(r'^message$', createPurchaseOrder_views.message, name='message'),
    re_path(r'^newPurchaseOrder$', createPurchaseOrder_views.newPurchaseOrder, name='newPurchaseOrder'),
    re_path(r'^purchaseOrderList$', viewPurchaseOrderStatus_views.purchaseOrderList, name='purchaseOrderList'),
    re_path(r'^poDetail$', viewPurchaseOrderStatus_views.poDetail, name='poDetail'),
    re_path(r'^purchaseOrderProductID$', createPurchaseOrder_views.purchaseOrderProductID, name='purchaseOrderProductID'),
    
    #Manager
    re_path(r'^viewPo/$', viewPo_views.viewPo, name='viewPo'),
    re_path(r'^viewPo$', viewPo_views.viewPo, name='viewPo'),
    re_path(r'^selectPo$', viewPo_views.selectPo, name='selectPo'),
    re_path(r'^searchPo$', viewPo_views.selectPo, name='searchPo'),
    re_path(r'^viewPo/searchPo$', viewPo_views.searchPo, name='searchPo'),
    re_path(r'^viewPo/selectPo$', viewPo_views.selectPo, name='selectPo'),
    re_path(r'^backtohome$', viewPo_views.backtohome, name='backtohome'),
    re_path(r'^backtolist$', viewPo_views.backtolist, name='backtolist'),
    re_path(r'^viewPo/backtohome$', viewPo_views.backtohome, name='backtohome'),
    re_path(r'^viewPo/backtolist$', viewPo_views.backtolist, name='backtolist'),
    re_path(r'^viewPo/approvePo$', viewPo_views.approvePo, name='approvePo'),
    re_path(r'^viewPo/rejectPo$', viewPo_views.rejectPo, name='rejectPo'),

    re_path(r'^arviewPo$', arviewPo_views.arviewPo, name='arviewPo'),
    re_path(r'^arviewPo/$', arviewPo_views.arviewPo, name='arviewPo'),
    re_path(r'^arviewPo/arsearchPo$', arviewPo_views.arsearchPo, name='arsearchPo'),
    re_path(r'^arviewPo/arselectPo$', arviewPo_views.arselectPo, name='arselectPo'),
    re_path(r'^arviewPo/arbacktohome$', arviewPo_views.arbacktohome, name='arbacktohome'),
    re_path(r'^arviewPo/arbacktolist$', arviewPo_views.arbacktolist, name='arbacktolist'),
    re_path(r'^arviewPo/arapprovePo$', arviewPo_views.arrejectPo, name='arrejectPo'),
    re_path(r'^arviewPo/arrejectPo$', arviewPo_views.arrejectPo, name='arrejectPo'),
    re_path(r'^arselectPo$', arviewPo_views.arselectPo, name='arselectPo'),
    re_path(r'^arsearchPo$', arviewPo_views.arsearchPo, name='arsearchPo'),
    re_path(r'^arbacktohome$', arviewPo_views.arbacktohome, name='arbacktohome'),
    re_path(r'^arbacktolist$', arviewPo_views.arbacktolist, name='arbacktolist'),
    re_path(r'^arapprovePo$', arviewPo_views.arapprovePo, name='arapprovePo'),
    re_path(r'^arrejectPo$', arviewPo_views.arrejectPo, name='arrejectPo'),
]