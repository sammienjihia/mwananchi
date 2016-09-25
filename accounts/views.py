from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm

def landing(request):
    title = "Landing"
    template = loader.get_template('accounts/landing.html')
    context = {"title": title}
    return HttpResponse(template.render(context, request))

def index(request):
    title = "Home"
    template = loader.get_template('accounts/index.html')
    context = {"title": title}
    return HttpResponse(template.render(context, request))

def login_view (request):
    title = "Login"
    template = loader.get_template('accounts/form.html')
    form = UserLoginForm(request.POST or None)
    context = {"form": form, "title": title}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/index")
    return HttpResponse(template.render(context, request))
    #return render(request, "form.html", {"form": form, "title": title})

def register_view (request):
    title = "Register"
    template = loader.get_template('accounts/form.html')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        newuser = authenticate(username=user.username, password=password)
        login(request, newuser)
        return redirect("/index")



    context = {"form": form, "title": title}
    return HttpResponse(template.render(context, request))

def logout_view (request):
    logout(request)
    return redirect("/")

# Create your views here.
