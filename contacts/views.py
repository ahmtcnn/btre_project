from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


# Create your views here.


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id = listing_id, name = name, email=email, phone=phone,
       message=message, user_id=user_id)
        

        # Check if user has made inquirt already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
        if has_contacted:
            messages.error(request, "You have already made an inquery for this listing")
        else:
            contact.save()
            messages.success(request, 'Your request has been submitted, realtor will get back to you soon')

            # Send email
            #  send_mail(
            #     'Property Listing Inquery',
            #     'There has been inquiry for ' + listing + '. Sign into your admin panel for more info',
            #     'ahmetcankaraagaclii@gmail.com',
            #     [realtor_email,'ahmetcankaraagaclii@hotmail.com'],
            #     fail_silently= False
            # )        


        return redirect('/listings/'+listing_id)
        
