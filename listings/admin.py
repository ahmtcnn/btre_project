from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publised', 'price', 'list_date', 'realtor') #listelere geldimizde hangi degerler siralansin
    list_display_links = ('id', 'title') # hangi degerlere tikladiginda link olsun
    list_filter = ('realtor',) #realtor a gore fiitreleme yapmak istiyosan
    #list_editable = ('is_publised',) liste uzerinde editleyebilecegin degerler
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25 #pagination


admin.site.register(Listing,ListingAdmin)


