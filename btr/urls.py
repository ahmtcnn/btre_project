from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Burada direk gidecegi fonksiyonu da belirtebiliriz veya bakacagi app url dosyasini da verebiliriz
urlpatterns = [
    path('',include('pages.urls')),  # We are linking to the url.py of the pages app
    path('listings/',include('listings.urls')), # if url start with listings/ go to listings.url and look for it
    path('accounts/',include('accounts.urls')),
    path('contacts/',include('contacts.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # fotolar için belirttik

#media file ların doğru şekilde çıkması için yaptık?