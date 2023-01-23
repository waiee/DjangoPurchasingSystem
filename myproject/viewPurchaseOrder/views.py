from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import render, redirect
from app.models import PurchaseOrder, PurchaseOrderProduct, Staff
from django.http import HttpRequest

@login_required
def viewPo(request):
    po_list = PurchaseOrder.objects.filter(selected=True).only('purchaseOrderID', 'staffID', 'poStatus')

    context = {
        'title':'View Purchase Order',
        'year':datetime.now().year,
        'po_list': po_list,
    }
    return render(request, 'viewPurchaseOrder/viewPo.html', context)

def selectPo(request):
    data = PurchaseOrder.objects.filter()
    po = None

    for i in data:
        if i.purchaseOrderID in request.POST:
            po = PurchaseOrder.objects.filter(purchaseOrderID=i.purchaseOrderID)
            products = PurchaseOrderProduct.objects.filter(purchaseOrderID=i.purchaseOrderID, productPurchased=True)
            qtyProvided = po.get().qtyProvided
            staffID = po.get().staffID
            vendorID = po.get().vendorID
            poStatus = po.get().poStatus
            totalPrice = po.get().totalPrice
    
    quo = po.get().quotationID
    
    context = {
        'po': po.get(), 'quo': quo, 
        'products': products, 
        'qtyProvided': qtyProvided,
        'staffID': staffID, 'vendorID':vendorID,
        'poStatus':poStatus, 'totalPrice': totalPrice,
    }

    return render(request,'viewPurchaseOrder/selectPo.html', context)

def approvePo(request):
    currentPo = PurchaseOrder.objects.filter(purchaseOrderID=request.POST.get("PurchaseOrder"))
    poStatus = request.POST.get("poStatus")

    if poStatus == "Pending":
        poStatus = "Approved"
    else:
        return render(request, 'viewPurchaseOrder/messagePo.html', context)
    currentPo.update()
    
    context = {
        'currentPo':currentPo, 'poStatus': poStatus           
    }

    return render(request, 'viewPurchaseOrder/messagePo.html', context)
##############################################################################################
def searchPo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        purchaseOrderID = PurchaseOrder.objects.filter(purchaseOrderID__contains=searched)

        context = {
                'searched': searched,
                'purchaseOrderID' : purchaseOrderID,
            }

        return render(request,'viewPurchaseOrder/searchPo.html',context)
    else:
        return render(request, 'viewPurchaseOrder/searchPo.html',context)

def backtoHome(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/menu.html',
            {
                'title':'View Item',
                'year': datetime.now().year,
            }
        )
def backtoList(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/viewPo/'))
    return render(
            request,
            'viewPurchaseOrder/viewPo.html',
            {
                'title':'Purchase Order List',
                'year': datetime.now().year,
            }
        )

