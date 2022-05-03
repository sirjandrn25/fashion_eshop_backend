from distutils.log import error
import imp
from django import forms
from store.models.auth import User
from django.contrib.auth.hashers import check_password,make_password




class LoginForm(forms.Form):
    email = forms.CharField(max_length=150,label="Email Address",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email address'}))
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = User.objects.filter(email=email).first()
        if user:
            if check_password(password,user.password):
                cleaned_data['user'] = user
                return cleaned_data
            else:
                errors = {
                    'password':['password is not matched !!!']
                }
        else:
            errors = {
                'email':['this email id does not exist !!!']
            }

        raise forms.ValidationError(errors)
            



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','contact_no','password']
        widgets = {
            'email':forms.EmailInput(attrs={'class':"form-control","placeholder":"Enter your email id"}),
            "password":forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter new password "}),
            "contact_no":forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Contact number"}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        contact_no = cleaned_data.get('contact_no')
        
        if len(password)<8:
            errors = {
                'password':['at least 8 charecters are required']
            }
        elif password.isdigit():
            errors = {
                'password':['only numeric values are not allowed']
            }
        elif len(contact_no) != 10:
            errors = {
                'contact_no':['10 digits most be required']
            }
        elif not contact_no:
            errors = {
                'contact_no':['only numeric values are allowed']
            }
        else:
            cleaned_data['password'] = make_password(password)
            return cleaned_data
        
        raise forms.ValidationError(errors)

    