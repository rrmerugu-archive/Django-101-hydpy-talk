from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'blog/$', views.blog_list, name="blog_list"),
    url(r'blogs-paginated/$', views.blog_list_paginated, name="blog_list_paginated"),
    url(r'blog/(?P<post_id>[0-9]+)$', views.blog_view, name="blog_view"),

]
