from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    # /music/
    url(r'^$', views.topic_to_keywords, name='search'),


]
