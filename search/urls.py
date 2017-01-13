from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    # /music/
    url(r'^$', views.searchwordview, name='search'),
    url(r'^results/$', views.results, name='results'),

]
