from django.urls import path
from Website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('NL', views.dutch, name='indexNL'),
    path('EN', views.english, name='indexEN'),
    path('Mail', views.sendmailtouser, name='sendMailNL'),
    path('Mailto', views.sendmailtouser, name='sendMailEN'),
    path('Resume', views.toResume, name='toResume'),
]