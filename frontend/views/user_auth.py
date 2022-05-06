from django.shortcuts import render,redirect
from frontend.forms.auth import *
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from frontend.decorators import custom_login_required

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request,user)
            redirect_url = request.session.get('after_login_url')
            
            if redirect_url is None:
                redirect_url = "index"
            
            return redirect(redirect_url)
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


# '_auth_user_id', '_auth_user_backend', '_auth_user_hash'
@custom_login_required(login_url="/user_login")
def userLogout(request):
    del request.session['_auth_user_id']
    del request.session['_auth_user_backend']
    del request.session['_auth_user_hash']
    del request.session['after_login_url'] 
    messages.success(request,"you are successfully logout")
    return redirect("user_login")