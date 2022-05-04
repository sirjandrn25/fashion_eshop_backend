from django.shortcuts import render,redirect
from frontend.forms.auth import *
from django.contrib.auth import login,logout
from django.contrib import messages

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
    else:
        context = {
            'form':LoginForm
        }
    
    return render(request,"auth/login.html",context)


def userRegisterView(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "successfully new user is register")
            return redirect("user_register")
        else:
            print(form.errors)
    else:
        context = {
            'form':UserRegisterForm
        }

    return render(request,"auth/register.html",context)


def userLogout(request):
    logout(request)
    return redirect("index")