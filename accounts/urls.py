from django.urls import path # if we want to define path we need to import this

from . import views # We are going to route url's to views's function so we need to import this

urlpatterns=[
    
    path('login',views.login,name='login'),  # /listings i ifade eder
    path('register',views.register,name='register'),  #/listings/23 gibi olmasını istiyoruz. listing_id parametresine erisiyoruz
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),

    # simdi ana url dosyasina dicezki eger /listings ile baslayan bir sey gorursen gel bu listings app in icindeki urls.py dosyasina bak
]