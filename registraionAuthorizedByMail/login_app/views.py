from django.shortcuts import render

# Create your views here.


def index(request) :
    diction = {'title':"Home Page"}
    return render(request, 'login_app/index.html',context=diction)


def login_attemp(request):
    diction = {"title":"Login Page"}
    
    return render(request, 'login_app/login.html', context=diction)
    
  
def rigister_attemp(request):
    diction = {"title":"Registration Page"}
    
    return render(request, 'login_app/register.html', context=diction)  