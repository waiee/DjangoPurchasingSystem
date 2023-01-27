from django.shortcuts import render
from app.models import Quotation
from app.models import Staff
from app.models import Vendor
from app.models import QuotationItem
from datetime import datetime
import random


# Create your views here.
def submitQuotation(request):

    quoIDgen = random.randint(0,4_000_000)
    staffList = Staff.objects.all()
    vendorList = Vendor.objects.all()

    context = {
        'title' : 'Submit Quotation Form',
        'year' : datetime.now().year,
        'staffList' : staffList,
        'vendorList' : vendorList,
        'quoIDgen' : quoIDgen,
    }

    return render(request, 'submitQuotation/submitQuotation.html', context)

def quotationConfirmation(request):
    if request.method == 'POST':
        newquo_id  = request.POST.get('quotationID')
        newstaff_id = Staff.objects.get(pk=request.POST.get('staffID'))
        newvalidity_date = request.POST.get('validityDate')
        newQuotation = Quotation(quotationID = newquo_id ,staffID = newstaff_id, validityDate =  newvalidity_date)
        newQuotation.save()

        context = {
            'quotationID': newQuotation.quotationID,
            'staffID': newQuotation.staffID.staffID,
            'validityDate': newQuotation.validityDate,
        }
    else:
        context = {
            'quotationID': None,
            'staffID': None,
            'validityDate': None,
        }
    return render(request, 'submitQuotation/quotationConfirm.html', context)

def addQuotationItem(request):
    if request.method == "GET":
        context = {
            'quotationID': request.GET.get('quotationID'),
            'itemID': random.randint(0, 4_000_000),
            'vendorList' : Vendor.objects.all(),
            'quoItemList': QuotationItem.objects.filter(quotationID=Quotation.objects.get(quotationID=request.GET.get('quotationID')))
        }
    else:  # assume post
        itemID = request.POST.get('itemID')
        quotationID = Quotation.objects.get(quotationID=request.POST.get('quotationID'))
        vendorID = Vendor.objects.get(vendorID= request.POST.get('vendorID'))
        itemName = request.POST.get('itemName')
        quantity = request.POST.get('quantity')
        itemPricePerUnit = request.POST.get('itemPriceperUnit')
        itemFinalPrice = request.POST.get('itemFinalPrice')

        newQuoItem = QuotationItem(itemID=itemID, quotationID=quotationID, vendorID = vendorID, itemName = itemName, quantity = quantity, itemPriceperUnit=itemPricePerUnit, itemFinalPrice = float(itemPricePerUnit) * int(quantity))
        newQuoItem.save()

        quotationID.totalPrice += float(newQuoItem.itemPriceperUnit) * int(newQuoItem.quantity)
        quotationID.save()

        

        context = {
            'quotationID': quotationID.quotationID,
            'itemID': random.randint(0, 4_000_000),
            'vendorList' : Vendor.objects.all(),
            'quoItemList': QuotationItem.objects.filter(quotationID=quotationID)
        }


    return render(request, 'submitQuotation/addItem.html', context)

def QuotationItemList(request):
    quoItemList = QuotationItem.objects.all()

    context = {
        'quoItemList' : quoItemList,
    }

    return render(request, 'submitQuotation/submitQuotation.html', context)


def quotationList(request):
    quoList = Quotation.objects.all()

    context = {
        'title': 'Quotation List' ,
        'quoList' : quoList,
    }

    return render(request, 'submitQuotation/quotationList.html', context)

def quotationDetail(request):

    if request.method == 'GET':
        context = {
            'quotationID' : request.GET.get('quotationID'),
            'quoItemList' : QuotationItem.objects.filter(quotationID=Quotation.objects.get(quotationID = request.GET.get('quotationID'))),
            'quoList' : Quotation.objects.filter(quotationID=Quotation.objects.get(quotationID = request.GET.get('quotationID'))),
        }

    else:
        quotationID = Quotation.objects.get(quotationID=request.POST.get('quotationID'))
        context ={
            'quotationID' : quotationID.quotationID,
            'quoItemList' : QuotationItem.objects.filter(quotationID=quotationID),
            'quoList' : Quotation.objects.filter(quotationID=quotationID),
        }

    quotationID = Quotation.objects.get(quotationID=request.POST.get('quotationID'))

    context ={
        'quotationID' : quotationID.quotationID,
        'quoItemList' : QuotationItem.objects.filter(quotationID=quotationID),
        'quoList' : Quotation.objects.filter(quotationID=quotationID),
    }

    return render(request, 'submitQuotation/quotationDetail.html', context)
