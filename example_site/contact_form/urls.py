from django.conf.urls import url
from contact_form import views

urlpatterns = [
    url(r'contact/$', views.contact_form, name="contact_form"),
]
