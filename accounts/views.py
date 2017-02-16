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
from subscribe.models import Subscribers
from sms.models import Blacklistsms, Outsms, Insms, Failedsms

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

def profile_view(request):
    title = "My Profile"
    template = loader.get_template('accounts/profile.html')
    #-----------top tile-------
    subscribers = [numbers.encode("utf8") for numbers in
                            Subscribers.objects.filter(subscribed_topic_id=request.user.id).values_list('mobile_number',
                                                                                                        flat=True).distinct()]
    sentsms = Outsms.objects.filter(sender=request.user.id).order_by('-sent_date')
    failedsms = Failedsms.objects.filter(sender=request.user.id).order_by('-sent_date')
    blacklistsms = Blacklistsms.objects.filter(sender=request.user.id).order_by('-sent_date')

    subscribers_count = len(subscribers)
    sentsms_count = len(sentsms)
    failedsms_count = len(failedsms)
    blacklistsms_count = len(blacklistsms)


    context = { "sentsms":sentsms, "failedsms":failedsms, "blacklistsms":blacklistsms, "subscribers": subscribers,
                "title": title,
                "subscribers_count":subscribers_count, "sentsms_count":sentsms_count, "failedsms_count":failedsms_count,
                "blacklistsms_count":blacklistsms_count}
    return HttpResponse(template.render(context, request))

# Create your views here.
