from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import *

# Create your views here


def purchaseOrderList(request):
    pl_list = PurchaseOrder.objects.all()
    context = {
        'title': 'Purchase Order List',
        'year': datetime.now().year,
        'pl_list': pl_list,
    }
    context['user'] = request.user

    return render(request,'purchaseOrderList.html',context)

def poDetail(request):
    podetail = None
    pd_list = PurchaseOrder.objects.filter()
    for i in pd_list:
        if i.purchaseOrderID in request.POST: 
            podetail = PurchaseOrder.objects.filter(purchaseOrderID=i.purchaseOrderID)
            product = PurchaseOrderProduct.objects.filter(purchaseOrderID=i.purchaseOrderID,productPurchased=True)
            qtyProvided = podetail.get().qtyProvided
            qtyNeeded = podetail.get().qtyNeeded
            staffID = podetail.get().staffID
            vendorID = podetail.get().vendorID
            poStatus = podetail.get().poStatus
            totalPrice = podetail.get().totalPrice
    context = {
        'title': 'Purchase Order Detail',
        'year': datetime.now().year,
        'podetail': podetail, 
        'product': product,
        'qtyProvided':qtyProvided,
        'qtyNeeded':qtyNeeded,
        'staffID': staffID,
        'vendorID' :vendorID,
        'poStatus':poStatus,
        'totalPrice': totalPrice,
    }

    return render(request,'poDetail.html',context)