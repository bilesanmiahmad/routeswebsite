from django.shortcuts import render
from .forms import DriverForm, ContactForm

# Create your views here.
def index(request):
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

