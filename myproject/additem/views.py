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
    newstaffID = request.POST['staffID']
    newvendorID = request.POST['vendorID']
    newvalidityDate = request.POST['validityDate']
    newqtyProvided = request.POST['qtyProvided']
    newtotalPrice= request.POST['totalPrice']

    newQuotation = Quotation(quotationID = newquotationID,
    staffID=newstaffID, vendorID= newvendorID,validityDate=newvalidityDate,
    qtyProvided= newqtyProvided, totalPrice = newtotalPrice,)
    newQuotation.save()

    context = {
        'quotationID': newquotationID, 'staffID': newstaffID,
        'vendorID': newvendorID, 'totalPrice': newtotalPrice,
        'validityDate': newvalidityDate, 'qtyProvided': newqtyProvided,
        'totalPrice': newtotalPrice,    
    }
    return render(request,'additem/additemconfirmation.html',context)

