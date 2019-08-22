from django.urls import path # if we want to define path we need to import this

from . import views # We are going to route url's to views's function so we need to import this

urlpatterns=[
    
    path('',views.index,name='listings'),  # /listings i ifade eder
    path('<int:listing_id>',views.listing,name='listing'),  #/listings/23 gibi olmasını istiyoruz. listing_id parametresine erisiyoruz
    path('search',views.search,name='search'),

    # simdi ana url dosyasina dicezki eger /listings ile baslayan bir sey gorursen gel bu listings app in icindeki urls.py dosyasina bak
]