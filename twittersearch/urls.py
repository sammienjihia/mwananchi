from django.conf.urls import url
from . import views

app_name = 'twittersearch'

urlpatterns = [
    # /music/
    url(r'^$', views.searchwordview, name='twittersearch'),
    url(r'^results/$', views.results, name='results'),

]
