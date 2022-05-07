from cProfile import label
from distutils.command.clean import clean
from email.policy import default
import imp
from django import forms



payment_choices = (
    ('PBC','Pay By Cash'),
    ('Khalti','Khalti'),
    ('Esewa','E-Sewa')
)
provinance_choices = (
    ('1','One'),
    ('2','Two'),
    ('3','Three'),
    ('4','Four'),
    ('5','Five')
)

class CheckoutForm(forms.Form):
    firstName = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),label="First Name"
    )
    lastName = forms.CharField(max_length=100,
     widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),label="Last Name"
    )
    contact_no = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'985462789'}))
    payment_way = forms.ChoiceField(choices=payment_choices,widget=forms.Select(attrs={'class':'form-select'}))

    address = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}))
    provinance_no = forms.ChoiceField(choices=provinance_choices,widget=forms.Select(attrs={'class':'form-select'}))
    city = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your city name'}))
    zip_code = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your zip code'}))
    street = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your street'}))

    save_delivery_address = forms.BooleanField(initial=True, required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input','checked':True}))

    def clean(self):
        cleaned_data = super().clean()
        contact_no = cleaned_data.get('contact_no')
        if not contact_no.isdigit():
            errors = {
                'contact_no':['only numeric values are allowed']
            }
        elif len(contact_no) != 10:
            errors = {
                'contact_no':['10 digits must be required']
            }
        else:
            return cleaned_data
        
        raise forms.ValidationError(errors)
