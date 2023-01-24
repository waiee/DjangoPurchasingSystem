from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Item, QuotationItem, Quotation

# Create your views here.

@login_required
def additemform(request):
    context = {
        'title': 'Add Item Form',
        'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request,'additem/additemform.html',context)

def additemconfirmation(request):

    newquotationID= request.POST['quotationID']
    newvalidityDate = request.POST['validityDate']
    newqtyProvided = request.POST['qtyProvided']
    newtotalPrice= request.POST['totalPrice']

    newQuotation = Quotation(quotationID = newquotationID,validityDate=newvalidityDate,
    qtyProvided= newqtyProvided, totalPrice = newtotalPrice,)
    newQuotation.save()

    context = {
        'quotationID': newquotationID,'totalPrice': newtotalPrice,
        'validityDate': newvalidityDate,'qtyProvided': newqtyProvided, 
    }
    return render(request,'additem/additemconfirmation.html',context)

def addnewitem(request):

    newquotationID= request.POST['quotationID']
    current_quo = request.POST.get(pk=newquotationID)
    newvendorID = request.POST['vendorID']
    current_ven = request.POST.get(pk=newvendorID)

    newitemID= request.POST['itemID']
    newitemName = request.POST['itemName']
    newitemPriceperUnit = request.POST['itemPriceperUnit']

    newItem = QuotationItem(quotationID = current_quo,
    itemID=newitemID, vendorID= newvendorID, itemName=newitemName,
    itemPriceperUnit= newitemPriceperUnit,)
    newItem.save()

    item_list = QuotationItem.objects.filter(quotationID=request.POST.get("quotationID"))

    context = {
        'quotationID': newquotationID, 'itemID': newitemID,
        'current_quo': current_quo, 'current_ven':current_ven,
        'vendorID': newvendorID, 'itemName': newitemName,
        'itemPriceperUnit': newitemPriceperUnit, 'item_list': item_list,
        'newItem': newItem,
    }
    return render(request,'additem/additemconfirmation.html',context)
