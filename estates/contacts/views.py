from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'admin@mail.ru',
    #   [realtor_email, 'contact@estates.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)

def editinq(request, id):
  contact = get_object_or_404(Contact, pk=id)

  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    contact_id = request.POST['id']

    contact = get_object_or_404(Contact, pk=contact_id)

    contact.name=name
    contact.email=email
    contact.phone=phone
    contact.message=message
    contact.user_id=user_id

    contact.save()

    return redirect('/accounts/dashboard')

  context = {
    'contact': contact
  }

  return render(request, 'contacts/editinq.html', context)

def delinq(request, id):
  contact = get_object_or_404(Contact, pk=id)

  if request.method == 'POST':

    contact_id = request.POST['id']

    contact = get_object_or_404(Contact, pk=contact_id)

    contact.delete()

    return redirect('/accounts/dashboard')

  context = {
    'contact': contact
  }

  return render(request, 'contacts/delinq.html', context)
