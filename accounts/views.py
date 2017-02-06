from django.http import HttpResponse, HttpResponseRedirect
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
    template = loader.get_template('accounts/login.html')
    form = UserLoginForm(request.POST or None)
    context = {"form": form, "title": title}

    if form.is_valid():
        #if request.is_ajax():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponse("/index")

    return HttpResponse(template.render(context, request))
    #return render(request, "form.html", {"form": form, "title": title})


# def login_view(request):
#     if request.method == 'POST':
#         request.session['username'] = request.POST['username']
#         request.session['password'] = request.POST['password']
#         user = authenticate(username=request.session['username'], password=request.session['password'])
#         username = request.session['username']
#         password = request.session['password']
#         if username and password:
#
#             if not user:
#                 return HttpResponse("User login is invalid")
#
#             elif not user.is_active:
#                 return HttpResponse("This user is no longer active")
#
#             else:
#                 login(request, user)
#         return redirect("/index")
#
#     else:
#         return render(request, 'accounts/login.html')

def register_view (request):
    title = "Register"
    template = loader.get_template('accounts/register.html')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        newuser = authenticate(username=user.username, password=password)
        login(request, newuser)
        return HttpResponse("/index")



    context = {"form": form, "title": title}
    return HttpResponse(template.render(context, request))

def logout_view (request):
    logout(request)
    return redirect("/")



# Create your views here.
