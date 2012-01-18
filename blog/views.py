from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader, Context

from blog.models import *

def get_entry(request, title_slug):
    entry = Entry.objects.get(title_slug=title_slug)
    return render_to_response('blog/blog_entry.html', RequestContext(request, locals()))

def projects(request):
    return render_to_response('blog/projects.html', RequestContext(request, locals()))