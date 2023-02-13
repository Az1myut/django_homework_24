from django.forms import forms
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactInfo, ContactMessage
from .forms import ContactMessageForm
from django.views.decorators.http import require_http_methods
import icecream as ic
# Create your views here.

def contact_info(request) -> render:
    template_ = 'contact_info.html'
    context = {
        'contact_info' : get_object_or_404(ContactInfo, pk=1),
        'contact_form' : ContactMessageForm(),
    }
    return render (request, template_, context=context)
@require_http_methods(['GET','POST'])
def contact_message(request) -> redirect:
    if request.method in "POST":

        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save() 
        else:
            template_ = 'contact_info.html'
            context = {
                'contact_info' : get_object_or_404(ContactInfo, pk=1),
                'contact_form' : ContactMessageForm(),
                'error':'Please use correct data'
            }
            return render (request, template_, context=context)

  
    return redirect('/contacts/')