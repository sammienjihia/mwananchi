from django.conf.urls import url
from . import views

app_name = 'twitterstream'

urlpatterns = [
    # /music/
    url(r'^$', views.stream, name='stream'),
    url(r'^streaming/$', views.streaming, name='streaming'),


]