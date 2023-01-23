from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Item, Quotation

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
    newtotalPrice= request.POST['totalPrice']
    newstaffID = request.POST['staffID']

    newQuotation = Quotation(quotationID = newquotationID,totalPrice = newtotalPrice, staffID=newstaffID)
    newQuotation.save()

    context = {
        'quotationID': newquotationID,
        'totalPrice': newtotalPrice,
        'staffID': newstaffID,
    }
    return render(request,'additem/additemconfirmation.html',context)

