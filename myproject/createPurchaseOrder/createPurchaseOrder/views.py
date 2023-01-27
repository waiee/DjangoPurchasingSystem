from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import *
import random

# Create your views here.
@login_required
def createPurchaseOrder(request): #nak pergi page createPurchaseOrder dari quotationDetail
    
    purchaseOrderID = random.randint(0,4_000_000)
    staffList = Staff.objects.all()
    vendorList = Vendor.objects.all()
    quotationID = Quotation.objects.get(quotationID=request.POST.get('quotationID'))

    context = {
        'staffList' : staffList,
        'vendorList' : vendorList,
        'purchaseOrderID' : purchaseOrderID,
        'quotationID' : quotationID,
    }
    
    return render(request,'createPurchaseOrder.html',context)

def poConfirmation(request):
    if request.method == 'POST':
        purchaseOrderID = request.POST.get('purchaseOrderID')
        quotationID = Quotation.objects.get(quotationID=request.POST.get('quotationID'))
        staffID = Staff.objects.get(pk=request.POST.get('staffID'))
        vendorID = Vendor.objects.get(vendorID= request.POST.get('vendorID'))
        qtyNeeded = request.POST.get('qtyNeeded')
        qtyProvided = request.POST.get('qtyProvided')
        totalPrice = request.POST.get('totalPrice')
        newPurchaseOrder = PurchaseOrder(purchaseOrderID = purchaseOrderID, quotationID = quotationID, staffID = staffID, vendorID = vendorID, qtyNeeded = qtyNeeded, qtyProvided = qtyProvided, totalPrice = totalPrice)
        newPurchaseOrder.save()

        context = {
            'quotationID' : newPurchaseOrder.quotationID,
            'purchaseOrderID' : newPurchaseOrder.purchaseOrderID,
            'staffID' : newPurchaseOrder.staffID,
            'vendorID' : newPurchaseOrder.vendorID,
            'qtyNeeded' : newPurchaseOrder.qtyNeeded,
            'qtyProvided' : newPurchaseOrder.qtyProvided,
            'totalPrice' : newPurchaseOrder.totalPrice
        }

    return render(request,'poConfirmation.html', context)
    
# ni nak pergi purchaseOrderdetail dari createPurchaseOrder
def purchaseOrderProductID(request): 
    current_po = PurchaseOrder.objects.filter(purchaseOrderID= request.POST.get("purchaseOrder"))
    productID = current_po.productID

    newPOP = PurchaseOrderProduct(productID=productID)
    newPOP.save()

    context={
        'productID':productID,
    }

    return render(request,'createPurchaseOrder.html',context)




def quotationList(request):
    ql_list = Quotation.objects.all()
    context = {
        'title': 'Quotation List',
        'year': datetime.now().year,
        'ql_list': ql_list,

    }
    context['user'] = request.user

    return render(request,'quotationList.html',context)

def quotationDetail(request):
    if request.method == 'GET':
        context = {
            'quotationID' : request.GET.get('quotationID'),
            'quoItemList' : QuotationItem.objects.filter(quotationID=Quotation.objects.get(quotationID = request.GET.get('quotationID'))),
            'quoList' : Quotation.objects.filter(quotationID=Quotation.objects.get(quotationID = request.GET.get('quotationID')))

        }
    else:
        quotationID = Quotation.objects.get(quotationID = request.POST.get('quotationID'))

        context = {
            'quotationID' : quotationID.quotationID,
            'quoItemList' : QuotationItem.objects.filter(quotationID=quotationID),
            'quoList' : Quotation.objects.filter(quotationID=quotationID),
        }


    return render(request,'quotationDetail.html',context)

def purchaseOrderDetail(request):
    # podetail = None
    # product = None
    # pd_list = PurchaseOrder.objects.filter()

    # for i in pd_list:
    #     if i.quotationID in request.POST: 
    #         podetail = PurchaseOrder.objects.filter(purchaseOrderID=i.purchaseOrderID)
    #         product = PurchaseOrderProduct.objects.filter(productID=i.productID,productPurchased=True)
    #         qtyProvided = podetail.get().qtyProvided
    #         qtyNeeded = podetail.get().qtyNeeded
    #         staffID = podetail.get().staffID
    #         vendorID = podetail.get().vendorID
    #         quotationStatus = podetail.get().quotationStatus
    #         totalPrice = podetail.get().totalPrice
    # context = {
    #     'title': 'Purchase Order Detail',
    #     'year': datetime.now().year,
    #     'podetail': podetail, 
    #     'product': product,
    #     'qtyProvided':qtyProvided,
    #     'qtyNeeded':qtyNeeded,
    #     'staffID': staffID,
    #     'vendorID' :vendorID,
    #     'poStatus':quotationStatus,
    #     'totalPrice': totalPrice,
    #     }
    # context['user'] = request.user
    quotationID = Quotation.objects.get(quotationID=request.POST.get('quotationID'))

    if request.method == 'GET':
        context = {
            'quotationID' : quotationID.quotationID,
            'quotationList' :  QuotationItem.objects.filter(quotationID=Quotation.objects.get(quotationID = request.GET.get('quotationID'))),
        }

    return render(request,'purchaseOrderDetail.html',context)

def message(request):
    context = {
        'title': 'Message',
        'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request,'message.html',context)

