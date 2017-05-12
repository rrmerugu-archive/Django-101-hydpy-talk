from django import forms
from contact_form.models import ContactEntry


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactEntry
        fields = ('subject', 'text')


