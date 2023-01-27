from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import Quotation, QuotationItem
from django.http import HttpRequest
from django.shortcuts import render, redirect

@login_required
def arviewquo(request):
    quotation_list = Quotation.objects.filter(selected=True).only('quotationID','staffID', 'quotationStatus')   

    context = {
        'title': 'Quotation List',
        'year': datetime.now().year,
        'quotation_list' : quotation_list,
    }

    return render(request, 'arQuotation/viewquotation.html', context)


def arselectquo(request):
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
        'quotation': quotation, 
        'item': item,
        'qtyProvided':qtyProvided,
        'staffID': staffID,
        'vendorID' :vendorID,
        'quotationStatus':quotationStatus,
        'totalPrice': totalPrice,
        'validityDate' : validityDate,
    }

    return render(request,'arQuotation/selectquo.html', context)


def arbacktoHome(request):
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

def arapprovequo(request):
    # currentquo = Quotation.objects.filter(quotationID=request.POST.get("quotation"))
    current_quo = Quotation.objects.filter(quotationID=request.POST.get("quotation"))
    print(current_quo)
    current_quo.update(quotationStatus='Approved')

    context = {
        'current_quo':current_quo,         
    }
    return render(request, 'arQuotation/message.html', context)

def arrejectquo(request):
    currentquo = Quotation.objects.filter(quotationID=request.POST.get("quotation"))
    print(currentquo)
    currentquo.update(quotationStatus='Rejected')

    context = {
        'currentquo':currentquo,         
    }
    return render(request, 'arQuotation/message.html', context)

def arbacktoList(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/arviewquo/'))
    return render(
            request,
            'arQuotation/viewquotation.html',
            {
                'title':'Quotation List',
                'year': datetime.now().year,
            }
        )

def arsearchquo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        quotationID = Quotation.objects.filter(quotationID__contains=searched)

        context = {
                'searched': searched,
                'quotationID' : quotationID,
            }

        return render(request,'arQuotation/searchquo.html',context)
    else:
        return render(request, 'arQuotation/searchquo.html',context)