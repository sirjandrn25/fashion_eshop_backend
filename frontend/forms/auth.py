import imp
from django import forms
from store.models.auth import User
from django.contrib.auth.hashers import check_password




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
    
    def clean(self,cleaned_data):
        print(cleaned_data)
    