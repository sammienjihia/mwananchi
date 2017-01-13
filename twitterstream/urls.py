from django.conf.urls import url
from . import views

app_name = 'twitterstream'

urlpatterns = [
    # /music/
    url(r'^$', views.tweetstream, name='tweetstream'),
    url(r'^download/$', views.download, name='download'),


    #url(r'^streaming/$', views.streaming, name='streaming'),


]