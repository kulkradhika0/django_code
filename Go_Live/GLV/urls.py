from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^setPasscode/', views.setPasscode, name='setPasscode'),
    url(r'^getPasscode/', views.getPasscode, name='getPasscode'),
    url(r'^addPasscode/', views.addPasscode, name='addPasscode'),
    url(r'^listUsers/', views.listUsers, name='listUsers'),
]
