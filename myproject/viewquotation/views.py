from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Quotation, QuotationItem, Staff
from django.http import HttpRequest
from django.shortcuts import render, redirect

@login_required
def viewquo(request):
    quotation_list = Quotation.objects.filter(selected=True).only('quotationID','staffID', 'quotationStatus')   

    context = {
        'title': 'Quotation List',
        'year': datetime.now().year,
        'quotation_list' : quotation_list,
    }

    return render(request, 'viewquotation/viewquotation.html', context)

def selectquo(request):
    data = Quotation.objects.filter()
    quotation = None

    for i in data:
        if i.quotationID in request.POST:
            quotation = Quotation.objects.filter(quotationID=i.quotationID)
            item = QuotationItem.objects.filter(quotationID=i.quotationID, itemPurchased=True)
            qtyProvided = quotation.get().qtyProvided
            staffID = quotation.get().staffID
            vendorID = quotation.get().vendorID
            quotationStatus = quotation.get().quotationStatus
            totalPrice = quotation.get().totalPrice
            validityDate = quotation.get().validityDate

    context = {
        'quotation': quotation.get(), 
        'item': item,
        'qtyProvided':qtyProvided,
        'staffID': staffID,
        'vendorID' :vendorID,
        'quotationStatus':quotationStatus,
        'totalPrice': totalPrice,
        'validityDate' : validityDate,
    }

    return render(request,'viewquotation/selectquo.html', context)

def approvequo(request):
    # currentquo = Quotation.objects.filter(quotationID=request.POST.get("quotation"))
    current_quo = Quotation.objects.filter(quotationID=request.POST.get("quotation"))
    print(current_quo)
    current_quo.update(quotationStatus='Approved')

    context = {
        'current_quo':current_quo,         
    }
    return render(request, 'viewquotation/message.html', context)

def rejectquo(request):
    current_quo = Quotation.objects.filter(quotationID=request.POST.get("quotation"))
    print(current_quo)
    current_quo.update(quotationStatus='Rejected')

    context = {
        'current_quo':current_quo,         
    }
    return render(request, 'viewquotation/message.html', context)

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
                'title':'View Quotation',
                'year': datetime.now().year,
            }
        )


def backtoList(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/viewquo/'))
    return render(
            request,
            'viewquotation/viewquotation.html',
            {
                'title':'Quotation List',
                'year': datetime.now().year,
            }
        )

def searchquo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        quotationID = Quotation.objects.filter(quotationID__contains=searched)

        context = {
                'searched': searched,
                'quotationID' : quotationID,
            }

        return render(request,'viewquotation/searchquo.html',context)
    else:
        return render(request, 'viewquotationr/searchquo.html',context)