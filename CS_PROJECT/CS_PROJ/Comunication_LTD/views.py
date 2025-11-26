import json
import string
import os
import re
from django.views import View
from django.utils.html import escape
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404


# Create your views here.
def home(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def loginFailed(request):
    return render(request, 'loginFailed.html')

def loginYAY(request):
    return render(request, 'loginYAY.html')

def register(request):
    return render(request, 'register.html')

def registerFailed(request):
    return render(request, 'registerFailed.html')

def registerConfirm(request):
    return render(request, 'registerConfirm.html')

def login_req(request):
    if(request.method == 'POST'):
        Uname = request.POST.get('username')
        safeUname = escape(Uname)
        password = request.POST.get('password')
        safePassword = escape(password)
    
    context = {}

    if(User.objects.filter(username=safeUname)).exists():

        if (authenticate(request=request, username = safeUname, password = safePassword)):
            return redirect('loginYAY')
        else:
            context.update({'reasonLogin' : 'Wrong password'})
            return render(request, 'loginFailed.html', context)
        
    context.update({'reasonLogin' : 'Wrong username or username does not exist'})
    return render(request, 'loginFailed.html', context)
        

    

def passwordValidator(password):
    with open(os.path.join(os.path.dirname(__file__), "passwordConfig.json"), "r") as file:
        passwordReq = json.load(file)

        if(len(password) == passwordReq['length'] and
          any(c.islower() for c in password) == passwordReq['lowerExist'] and
          any(c.isupper() for c in password) == passwordReq['upperExist'] and
          any(c.isdigit() for c in password) == passwordReq['digitExist'] and
          any(c in string.punctuation for c in password) == passwordReq['specialExist']):
            return True
        
        else:
            return False
    
def register_req(request):
    if(request.method == 'POST'):

        Uname = request.POST.get('username')
        safeName = escape(Uname)

        email = request.POST.get('email')
        safeEmail = escape(email)

        password = request.POST.get('password')
        safePassword = escape(password)

        confirmPassword = request.POST.get('confirmPassword')
        confirmPassword = escape(confirmPassword)

        context = {}

        if(User.objects.filter(username=safeName).exists()):
            context.update({'reasonLogin' : 'This name is already in use'})
            return render(request, 'registerFailed.html', context)

        if not (re.match(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}$', safeEmail)):
            context.update({'reasonLogin' : 'Invalid email'})
            return render(request, 'registerFailed.html', context)
        
        if(User.objects.filter(email=safeEmail).exists()):
            context.update({'reasonLogin' : 'This email is already in use'})
            return render(request, 'registerFailed.html', context)

        if(passwordValidator(safePassword) == True):
        
            if(safePassword == confirmPassword):
                user = User.objects.create_user(safeName, safeEmail, safePassword)
                user.save()
                return redirect('registerConfirm')
            else:  
                context.update({'reasonLogin' : 'Passwords didn\'t match'})
                return render(request, 'registerFailed.html', context)
            
        else:
            context.update({'reasonLogin' : 'Password didn\'t meet the requirements'})
            return render(request, 'registerFailed.html', context)