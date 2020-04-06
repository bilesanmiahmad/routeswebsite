from django import forms

MODEL_CHOICES = (('Mercedez', 'Mercedez'), ('BMW', 'BMW'), ('Toyota', 'Toyota'), ('Honda', 'Honda'))
COLORS = (('Black', 'Black'), ('White', 'White'), ('Grey', 'Grey'), ('Silver', 'Silver'),
          ('Red', 'Red'), ('Burgundy', 'Burgundy'), ('Blue', 'Blue'), ('Light Blue', 'Light Blue'), ('Green', 'Green'),
          ('Gold', 'Gold'))
YEAR = (('1999', 1999), ('2000', 2000), ('2001', 2001), ('2002', 2002), ('2003', 2003), ('2004', 2004), ('2005', 2005),
        ('2006', 2006), ('2007', 2007), ('2008', 2008), ('2009', 2009), ('2010', 2010), ('2011', 2011), ('2012', 2012),
        ('2013', 2013), ('2014', 2014), ('2015', 2015), ('2016', 2016), ('2017', 2017), ('2018', 2018), ('2019', 2019),
        ('2020', 2020))
DOOR = (('2-Doors', 2), ('4-Doors', 4))

STATE = (('Lagos', 'Lagos'),)


class PersonalDataForm(forms.Form):
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
        required=True, label="Mobile Number",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    password = forms.CharField(required=True, label="Password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    state = forms.CharField(required=True, label="State",
                               widget=forms.Select(attrs={'class': 'form-control'}, choices=STATE))


class OTPForm(forms.Form):
    otp = forms.CharField(required=True, label="OTP",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserting OTP'}))


class CarDriverForm(forms.Form):
    profile_picture = forms.ImageField(
        required=True, label="Profile Picture", widget=forms.FileInput(attrs={'class': 'form-control'}))

    driver_license = forms.ImageField(
        required=True, label="Driver's License", widget=forms.FileInput(attrs={'class': 'form-control'}))
    model = forms.CharField(required=True, label="Car Model",
                            widget=forms.Select(attrs={'class': 'form-control'}, choices=MODEL_CHOICES))
    color = forms.CharField(required=True, label="ar Color",
                            widget=forms.Select(attrs={'class': 'form-control'}, choices=COLORS))
    year = forms.IntegerField(required=True, label="Car Year",
                              widget=forms.Select(attrs={'class': 'form-control'}, choices=YEAR))
    door = forms.IntegerField(required=True, label="Car Door",
                              widget=forms.Select(attrs={'class': 'form-control'}, choices=DOOR))
    plate_number = forms.CharField(max_length=30, required=True, label="Plate Number",
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Plate Number'}))
    vehicle_license = forms.ImageField(required=True, label="Vehicle License",
                                       widget=forms.FileInput(attrs={'class': 'form-control'}))
    road_worthiness = forms.ImageField(required=True, label="Road Worthiness Certificate",
                                       widget=forms.FileInput(attrs={'class': 'form-control'}))
    insurance = forms.ImageField(required=True, label="Car Insurance",
                                 widget=forms.FileInput(attrs={'class': 'form-control'}))
    inspection_report = forms.ImageField(required=True, label="Inspection Report",
                                         widget=forms.FileInput(attrs={'class': 'form-control'}))


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=60, min_length=2, required=True,
        label="Full Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(
        required=True, label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
