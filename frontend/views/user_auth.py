from django.shortcuts import render,redirect
from frontend.forms.auth import *
from django.contrib.auth import login

def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request,user)

            return redirect("user_login")
        
        return render(request,"auth/login.html",context)

    context = {
        'form':LoginForm
    }
    

    return render(request,"auth/login.html",context)


def userRegisterView(request):
    context = {
        'form':UserRegisterForm
    }

    return render(request,"auth/register.html",context)