from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import Http404, HttpResponse
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth 

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'html_files/index.htm')
        else:
            return render(request,'html_files/Login.htm',{'error':"invalid data."})
    else:
        return render(request,'html_files/Login.htm')

def logout(request):
    if request=="POST":
        logout(request)
        return redirect('login')