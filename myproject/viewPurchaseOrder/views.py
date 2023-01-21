from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect
from app.models import QuotationItem, PurchaseOrder
from django.http import HttpRequest

@login_required

def viewPo(request):
    po_list = PurchaseOrder.objects.all()

    return render(
        request,
        'viewPurchaseOrder/viewPo.html',
        {
            'title':'View Purchase Order',
            'year':datetime.now().year,
            'po_list' : po_list,
        }
    )

def selectPo(request, purchaseOrderID):
    if request.method == "POST":
        selected = request.POST['selected']
        purchaseOrderID = PurchaseOrder.objects.get(purchaseOrderID = purchaseOrderID)

        return render(
            request,
            'viewPurchaseOrder/selectPo.html',
            {
                'selected': selected,
                'purchaseOrderID' : purchaseOrderID,
            }
        )
    else:
        return render(request, 
        'viewPurchaseOrder/selectPo.html',{})

def searchPo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        purchaseOrderID = PurchaseOrder.objects.filter(purchaseOrderID__contains=searched)
        return render(
            request,
            'viewPurchaseOrder/searchPo.html',
            {
                'searched': searched,
                'purchaseOrderID' : purchaseOrderID,
            }
        )
    else:
        return render(request, 
        'viewPurchaseOrder/searchPo.html',{})

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