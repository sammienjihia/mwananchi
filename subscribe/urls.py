from django.conf.urls import url
from . import views

app_name = 'subscribe'

urlpatterns = [
    # /music/
    url(r'^$', views.subscriptionview, name='subscribe'),


]