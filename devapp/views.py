from django.shortcuts import redirect, render
from django.contrib import messages


from .forms import *
# Create your views here.
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def registration(request):
    return render(request, 'registration.html')


#contact 
def contact(request):
    cform = ContactForm() #instantiate an empty form for a GET request
    if request.method == 'POST':
        cform = ContactForm(request.POST)#instantiate the form for a POST request
        if cform.is_valid():
            cform.save()
            messages.success(request, 'Thank you for contacting us, Our Customer Care will reach you soon😊')
            return redirect('index')
        else:
            messages.error(request, cform.errors)
            return redirect('index')
    
    context = {
        'cform':cform
    }
    
    return render(request,'index.html', context)
#contact done

#registration 
def registration(request):
    cform = RegistrationForm() #instantiate an empty form for a GET request
    if request.method == 'POST':
        cform = RegistrationForm(request.POST)#instantiate the form for a POST request
        if cform.is_valid():
            cform.save()
            messages.success(request, "We'll Get Back To You Soon, Thank You.")
            return redirect('index')
        else:
            messages.error(request, cform.errors)
            return redirect('index')
    
    context = {
        'cform':cform
    }
    
    return render(request,'registration.html', context)
#contact done