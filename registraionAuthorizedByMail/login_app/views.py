import uuid
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from login_app import models
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def index(request) :
    diction = {'title':"Home Page"}
    return render(request, 'login_app/index.html',context=diction)


def login_attemp(request):
    diction = {"title":"Login Page"}
    
    return render(request, 'login_app/login.html', context=diction)
    
  
def rigister_attemp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            if User.objects.filter(username=username).first():
            
                messages.warning(request, "This user is already exsist!!")
                return HttpResponseRedirect(reverse('login_app:register_attempt'))
            if User.objects.filter(email=email).first():
            
                messages.warning(request, "This email already taken !!")
                return HttpResponseRedirect(reverse('login_app:register_attempt'))
            
            user_obj = User(username=username, email=email) 
            user_obj.set_password(password)
            user_obj.save()
            profile_obj = models.Profile.objects.create(user=user_obj, auth_token=str(uuid.uuid4()))
            profile_obj.save()
            return HttpResponseRedirect(reverse('login_app:token_send'))
            
        except Exception as e:
            print(e)
    diction = {"title":"Registration Page"}
    
    return render(request, 'login_app/register.html', context=diction)  

def token_send(request):
    
    return render(request, 'login_app/token.html',context={})

def success(request):
    return render(request, 'login_app/success.html',context={})