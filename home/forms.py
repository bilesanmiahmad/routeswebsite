from django import forms


class DriverForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, required=True, 
        label="First Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        max_length=30, required=True, 
        label="Last Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(
        required=True, label="Email", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    phone = forms.CharField(
        required=True, label="Contact Phone", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    driver_license = forms.ImageField(
        required=True, label="Driver's License", 
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    profile_picture = forms.ImageField(
        required=True, label="Profile Picture", 
        widget=forms.FileInput(attrs={'class': 'form-control'}))


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=60, min_length=2, required=True, 
        label="Full Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(
        required=True, label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
