from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.

def index(request):
    rc = RequestContext(request)
    context = {}

    response = render_to_response('index.html', context, rc)
    return response
