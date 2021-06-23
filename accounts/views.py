from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

def SignIpFirst(request) :

    if request.method =="POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username == '' :
            messages.info(request,'Введены некоректные данные ')
            return redirect("/accounts/login/signup")
        if password1 == password2 :
            if User.objects.filter(username=username).exists() :
                if (len(username)>12) :
                    messages.info(request,"Имя пользователя слишком длинное")
                    return redirect( '/accounts/login/signup' )
                else :
                    messages.info(request,'Имя пользователя уже занято ')
                    return redirect('/accounts/login/signup')
            else :
                user = User.objects.create_user(username=username , password = password1)
                user.save()
                return redirect('/accounts/login')
        else :
            messages.info(request,'Пароли не совпадают')
            return redirect('/accounts/login/signup')
    else :pass
    return render(request,'signup.html')