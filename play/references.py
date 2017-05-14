from django.db import models
class BlogPost(models.Model):
    pass# ... fields here


from django.test import TestCase
from django.core.urlresolvers import reverse
class ContactFormTest(TestCase):

    def test_good_contact_form(self):
        """
        Tests if a success message is returned when valid data is posted
        :return:
        """
        res = self.client.post(reverse('contact_form'),
                               {'subject': 'Hello help me', 'text': 'my machine is not working'})
        messages = [m.message for m in list(res.context["messages"])]
        self.assertIn("Your request submitted successfully", messages)




from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver
# method for post_save
@receiver(post_save, sender=BlogPost)
def update_post(sender, instance, created, **kwargs):
    if created:
        pass # on first time creation send email notif
    else:
         instance.visitors_count += 1
         instance.save()
         
         


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#https://docs.djangoproject.com/en/1.11/howto/static-files/