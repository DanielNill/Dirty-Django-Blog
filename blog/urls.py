from django.conf.urls.defaults import patterns, include, url

from blog import views

urlpatterns = patterns('',
    url(r'(?P<title_slug>[a-zA-Z0-9_.-]+)/', views.get_entry),
    url(r'^projects/', views.projects),
    url(r'^contact/', views.projects),
)