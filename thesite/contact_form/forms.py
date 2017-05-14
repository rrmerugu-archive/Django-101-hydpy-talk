from django import forms
from .models import ContactEntry


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactEntry
        fields = ('subject', 'text')
