from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import PersonalDataForm, ContactForm, CarDriverForm, OTPForm


# Create your views here.


def index(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            fname = contact_form.cleaned_data['full_name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            send_mail(
                'Client Request Email from' + fname + 'with email' + email,
                message,
                'customersupport@connectroutes.com',
                ['abilesanmi@connectroutes.com', 'customersupport@connectroutes.com']
            )
        return redirect('home')

    contact_form = ContactForm()
    return render(request, 'home/index.html', {'contact': contact_form})


def driver_registration(request):
    if request.method == 'POST':
        reg_form = PersonalDataForm(request.POST)
        if reg_form.is_valid():
            first_name = reg_form.cleaned_data['first_name']
            print('first name', first_name)
            last_name = reg_form.cleaned_data['last_name']
            email = reg_form.cleaned_data['email']
            phone = reg_form.cleaned_data['phone']
            password = reg_form.cleaned_data['password']
            state = reg_form.cleaned_data['state']
            request.session['reg_form'] = {'first_name': first_name, 'last_name': last_name, 'email': email,
                                           'phone': phone, 'password': password, 'state': state}
        print(request.session.get('reg_form'))
        return redirect('otp-reg')
    reg_form = PersonalDataForm()
    return render(request, 'home/driver_registration.html', {'reg_form': reg_form})


def vehicle_registration(request):
    car_form = CarDriverForm()
    return render(request, 'home/car_reg.html', {'car_form': car_form})


def otp_registration(request):
    if request.method == 'POST':
        otp_form = OTPForm(request.POST)
        if otp_form.is_valid():
            pass
        return redirect('car-reg')
    otp_form = OTPForm()
    return render(request, 'home/otp.html', {'otp_form': otp_form})


def faq(request):
    return render(request, 'home/faq.html')


def service(request):
    return render(request, 'home/terms_service.html')


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')


def quiz(request):
    return render(request, 'home/quiz.html')


def about(request):
    return render(request, 'home/about.html')
