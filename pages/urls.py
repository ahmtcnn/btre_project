from django.urls import path # if we want to define path we need to import this

from . import views # We are going to route url's to views's function so we need to import this

urlpatterns=[
    path('about',views.about,name='about'),
    path('',views.index,name='index'),
    

]