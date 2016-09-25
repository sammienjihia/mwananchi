from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    # /music/
    url(r'^$', views.topics, name='search'),


]
