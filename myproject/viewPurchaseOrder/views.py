from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect
from app.models import PurchaseOrder, PurchaseOrderProduct
from django.http import HttpRequest
from django import user

@login_required

def viewPo(request):
    po_id = PurchaseOrder.objects.get(user=request.user).purchaseOrderID

    PO = PurchaseOrder.objects.filter(purchaseOrderID=po_id)
    po_items = PurchaseOrderProduct.objects.all().values()

    print(po_items)
    context = {
        'title':'View Purchase Order',
        'year':datetime.now().year,
        'PO': PO,
        'po_items': po_items,
    }

    return render(request, 'viewPurchaseOrder/viewPo.html', context)

def selectPo(request, purchaseOrderID):
    selected_po_id = PurchaseOrder.objects.get(purchaseOrderID=purchaseOrderID)

    po_items = PurchaseOrderProduct.objects.filter(purchaseOrderID=selected_po_id) 
    print(po_items)

    context = {
        'selected_po_id': selected_po_id,
        'po_items' : po_items,
    }

    return render(request,'viewPurchaseOrder/selectPo.html', context)

##############################################################################################
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

# def view_PO(request):
#     fo_id = FinanceOfficer.objects.get(user=request.user).finance_officer_id

#     PO = PurchaseOrder.objects.filter(finance_officer_id=fo_id)
#     Po_item = POItems.objects.all().values()

#     print(Po_item)
#     context = {
#         'PO': PO,
#         'PO_item': Po_item
#     }

#     return render(request, 'PurchaseOrder/viewPO.html', context)


# def view_one_PO(request, po_id):
#     select_po_id = PurchaseOrder.objects.get(po_id=po_id)

#     PO_item = POItems.objects.filter(po_id=select_po_id)

#     print(PO_item)
#     context = {
#         'selected_po': select_po_id,
#         'PO_item': PO_item
#     }
#     return render(request, 'PurchaseOrder/viewOnePO.html', context)