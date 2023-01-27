from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import PurchaseOrder, PurchaseOrderProduct, Staff
from django.http import HttpRequest

@login_required
def arviewPo(request):
    po_list = PurchaseOrder.objects.filter(selected=True).only('purchaseOrderID', 'staffID', 'poStatus')

    context = {
        'title':'View Purchase Order',
        'year':datetime.now().year,
        'po_list': po_list,
    }
    return render(request, 'arPurchaseOrder/viewPo.html', context)

def arselectPo(request):
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
            print(poStatus)
    
    quo = po.get().quotationID 

    context = {
        'po': po.get(), 'quo': quo, 
        'products': products, 
        'qtyProvided': qtyProvided,
        'staffID': staffID, 'vendorID':vendorID,
        'poStatus':poStatus, 'totalPrice': totalPrice,
    }

    return render(request,'arPurchaseOrder/selectPo.html', context)

def arapprovePo(request):
    #DATA BEFORE
    # dataP = PurchaseOrder.objects.filter(poStatus__in=['Pending']).values()
    # dataAp = PurchaseOrder.objects.filter(poStatus__in=['Approved']).values()
    # print(dataP)
    # print(dataAp)

    #GET SELECTED PO
    currentPo = PurchaseOrder.objects.filter(purchaseOrderID=request.POST.get("purchaseOrder"))
    print(currentPo)
    currentPo.update(poStatus='Approved')

    #DATA AFTER
    # print(dataP)
    # print(dataAp)

    context = {
        'currentPo':currentPo         
    }
    return render(request, 'arPurchaseOrder/messagePo.html', context)

def arrejectPo(request):
    #DATA BEFORE
    # dataP = PurchaseOrder.objects.filter(poStatus__in=['Pending']).values()
    # dataAp = PurchaseOrder.objects.filter(poStatus__in=['Approved']).values()
    # print(dataP)
    # print(dataAp)

    #GET SELECTED PO
    currentPo = PurchaseOrder.objects.filter(purchaseOrderID=request.POST.get("purchaseOrder"))
    print(currentPo)
    currentPo.update(poStatus='Rejected')

    #DATA AFTER
    # print(dataP)
    # print(dataAp)

    context = {
        'currentPo':currentPo         
    }
    return render(request, 'arPurchaseOrder/messagePo.html', context)

##############################################################################################
def arsearchPo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        purchaseOrderID = PurchaseOrder.objects.filter(purchaseOrderID__contains=searched)

        context = {
                'searched': searched,
                'purchaseOrderID' : purchaseOrderID,
            }

        return render(request,'arPurchaseOrder/searchPo.html',context)
    else:
        return render(request,'arPurchaseOrder/searchPo.html',context)

def arbacktohome(request):
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
def arbacktolist(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/arviewPo/'))
    return render(
            request,
            'arPurchaseOrder/viewPo.html',
            {
                'title':'Purchase Order List',
                'year': datetime.now().year,
            }
        )

