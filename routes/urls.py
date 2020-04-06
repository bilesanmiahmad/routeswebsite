"""routes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from home import views as hv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', hv.index, name='home'),
    path('driver-registration', hv.driver_registration, name="driver-reg"),
    path('vehicle-registration', hv.vehicle_registration, name="car-reg"),
    path('otp-registration', hv.otp_registration, name='otp-reg'),
    path('faqs', hv.faq, name='faq'),
    path('terms-of-service', hv.service, name='service'),
    path('privacy-policy', hv.privacy_policy, name='policy'),
    path('quiz', hv.quiz, name='quiz'),
    path('about', hv.about, name='about'),
]
