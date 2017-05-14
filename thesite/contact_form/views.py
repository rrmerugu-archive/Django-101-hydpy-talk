# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def contact_form_view(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Awesome")
        else:
            messages.error(request, "error found")
            
    else:
        form = ContactForm()
    return render(request,'contact-form.html',
                  {'form': form})
