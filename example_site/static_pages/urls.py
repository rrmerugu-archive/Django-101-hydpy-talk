from django.conf.urls import url
from static_pages import views

urlpatterns = [
    url(r'$', views.home_page, name="home_page"),
]
