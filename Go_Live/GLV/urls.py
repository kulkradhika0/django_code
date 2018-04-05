from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^setPasscode/', views.setPasscode, name='setPasscode'),
    url(r'^getPasscode/', views.getPasscode, name='getPasscode'),
]
