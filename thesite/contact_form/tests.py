from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from .forms import ContactForm, ContactEntry


# Create your tests here.


class ContactFormTest(TestCase):
    def test_good_contact_form(self):
        """
        Tests if a success message is returned when valid data is posted
        :return:
        """
        res = self.client.post(reverse('contact_form_view'),
                               {'subject': 'Hello help me', 'text': 'my machine is not working'})
        messages = [m.message for m in list(res.context["messages"])]
        self.assertIn("Awesome", messages)
    
    def test_bad_contact_form(self):
        """
        Tests if a error message is returned when invalid data is posted

        :return:
        """
        res = self.client.post(reverse('contact_form_view'),
                               {'text': 'my machine is not working'})
        messages = [m.message for m in list(res.context["messages"])]
        self.assertIn("error found", messages)
    
    def test_contact_valid_form(self):
        entry = ContactEntry.objects.create(subject="help please", text="yes, this is only a test")
        data = {'subject': entry.subject, 'text': entry.text, }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())
    
    def test_contact_invalid_form(self):
        entry = ContactEntry.objects.create(text="yes, this is only a test")
        data = {'subject': entry.subject, 'text': entry.text, }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())