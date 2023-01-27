from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            # 'message':'Dr. Yeoh.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Purchasing System',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

@login_required
def menu(request):
    check_purchaser = request.user.groups.filter(name='purchaser').exists()
    check_employee = request.user.groups.filter(name='employee').exists()
    check_financeofficer = request.user.groups.filter(name='finance officer').exists()
    check_manager = request.user.groups.filter(name='manager').exists()

    context = {
            'title':'Main Menu',
            'year':datetime.now().year,
            'is_purchaser': check_purchaser,
            'is_employee': check_employee,
            'is_financeofficer': check_financeofficer,
            'is_manager': check_manager,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)