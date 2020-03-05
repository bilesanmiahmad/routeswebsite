from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import DriverForm, ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            fname = contact_form.cleaned_data['full_name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            send_mail(
                f'Client Request Email from {fname} with email {email}',
                message,
                'customersupport@connectroutes.com',
                ['abilesanmi@connectroutes.com', 'customersupport@connectroutes.com']
            )
        return redirect('home')
    
    contact_form = ContactForm()
    return render(request, 'home/index.html', {'contact': contact_form})


def driver_registration(request):
    reg_form = DriverForm()
    return render(request, 'home/driver_registration.html', {'reg_form': reg_form})


def faq(request):
    return render(request, 'home/faq.html')

def service(request):
    return render(request, 'home/terms_service.html')

def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')

def quiz(request):
    return render(request, 'home/quiz.html')

