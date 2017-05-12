# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from contact_form.forms import ContactForm
from django.contrib import messages
# Create your views here.


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request submitted successfully')
        else:
            messages.error(request, 'Please fix the errors and re-submit')
    else:
        form = ContactForm()
    return render(request, "contact-form.html", {"form": form})