from django.conf.urls.defaults import patterns, include, url

from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context

from blog.models import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def projects(request):
    return render_to_response('blog/projects.html')

def contact(request):
    return render_to_response('blog/contact.html')
        
def home(request):
    entries = Entry.objects.all().order_by('date')
    image = Media.objects.get(id=2)
    return render_to_response('blog/home.html', RequestContext(request, locals()))

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', projects),
    url(r'^contact/', contact),
    url(r'^$', home),
    url(r'^blog/', include('DanielNill.blog.urls')),    
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), 
)
