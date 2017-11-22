from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import PostForm
from theWall.models import Post

# Create your views here.

def index(request):
    rc = RequestContext(request)
    posts = Post.objects.all()
    context = {}

    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.content = "nope" # replace this with the cipher.
            post.save()

            return HttpResponseRedirect('/')
        else:
            pass
    else:
        form = PostForm()
    context['form'] = form
    context['posts'] = posts
    response = render_to_response('index.html', context, rc)
    return response
