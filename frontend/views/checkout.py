import imp
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login_user")
def checkout_view(request):

    return render(request,"home/checkout.html")