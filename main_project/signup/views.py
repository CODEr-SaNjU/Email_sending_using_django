from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import Http404, HttpResponse
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth 

def signup(request):
    if request.method=='POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return  redirect('signup')
            else:
                user = User.objects.create_user(email=email,username=username,password=password)
                user.save();
                messages.success(request,'registration has been successfully completed')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('signup')
    else:
        return render(request,'html_files/index.htm')
        # return render(request,'html_files/signup.htm')