from django.conf.urls import url
from . import views
from .views import (login_view, logout_view, register_view)


app_name = 'accounts'

urlpatterns = [
    # /music/
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^index/', views.index, name='index'),
    url(r'^profile/', views.profile_view, name='profile'),
    url(r'^$', views.landing, name='landing')

]
