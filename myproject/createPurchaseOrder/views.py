from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import *
import random

# Create your views here.
@login_required
def createPurchaseOrder(request): #nak pergi page createPurchaseOrder dari quotationDetail
    
    # quo = None
    # quoItem =None
    # newQuantity = 0
    # quoItemList = Quotation.objects.filter()
    
    # # for i in quoItemList:
    # #     if i.quotationID in request.POST:
    # quo = Quotation.objects.filter(quotationID =request.POST.get("quotationID"))
    # quoItem = QuotationItem.objects.filter(quotationID=request.POST.get("quotationID"))
    # newQuantity = quoItem.get().quantity
    # print(quo) 
    # print(quoItem)

    context = {
        # 'quoItem':quoItem,
        # 'quo': quo,
        # 'quoItemList' : quoItemList,
        'quotationID' : request.GET.get('quotationID'),
        
        # 'newQuantity' : newQuantity,
    }
    return render(request,'createPurchaseOrder.html',context)

def newPurchaseOrder(request):
    newpurchaseOrderID = request.POST['purchaseOrderID']
    newqtyProvided = request.POST['qtyProvided']
    newqtyNeeded = request.POST['qtyNeeded']
    newtotalPrice = request.POST['totalPrice']

    newPO = PurchaseOrder(purchaseOrderID = newpurchaseOrderID, 
    qtyProvided = newqtyProvided, 
    qtyNeeded=newqtyNeeded, totalPrice= newtotalPrice)
    newPO.save()

    context = {

        'purchaseOrderID': newpurchaseOrderID,
        'qtyProvided': newqtyProvided,
        'qtyNeeded': newqtyNeeded,
        'totalPrice' : newtotalPrice,
        }
    return render(request,'poConfirmation.html',context)
    
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
    podetail = None
    product = None
    pd_list = PurchaseOrder.objects.filter()

    for i in pd_list:
        if i.quotationID in request.POST: 
            podetail = PurchaseOrder.objects.filter(purchaseOrderID=i.purchaseOrderID)
            product = PurchaseOrderProduct.objects.filter(productID=i.productID,productPurchased=True)
            qtyProvided = podetail.get().qtyProvided
            qtyNeeded = podetail.get().qtyNeeded
            staffID = podetail.get().staffID
            vendorID = podetail.get().vendorID
            quotationStatus = podetail.get().quotationStatus
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
        'poStatus':quotationStatus,
        'totalPrice': totalPrice,
        }
    context['user'] = request.user

    return render(request,'purchaseOrderDetail.html',context)

def message(request):
    context = {
        'title': 'Message',
        'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request,'message.html',context)

