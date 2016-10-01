from django.conf.urls import url
from . import views

app_name = 'sms'

urlpatterns = [
    # /music/
    url(r'^$', views.sendsmsview, name='sendsms'),


]