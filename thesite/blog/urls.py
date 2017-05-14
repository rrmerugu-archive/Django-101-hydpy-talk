from django.conf.urls import url
from . import views
from contact_form.views import contact_form_view
urlpatterns = [
    url(r'blog/(?P<post_id>[0-9]+)/$', views.blog_view,
        name="blog_view"),
    
    url(r'blog/$', views.blog_list, name="blog_list"),
    
    url(r'contact/$',
        contact_form_view,
        name="contact_form_view"),
    url(r'$', views.index_page, name="index_page"),

]