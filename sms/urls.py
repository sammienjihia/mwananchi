from django.conf.urls import url
from . import views

app_name = 'sms'

urlpatterns = [
    # /music/
    url(r'^$', views.smssearchwordview, name='searchsms'),
    url(r'^sendsms/$', views.sendsmsview, name='sendsms'),
    url(r'^insms/$', views.insmsview, name='insms'),


]