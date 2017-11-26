from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import PostForm, KeyForm
from theWall.models import *

# Create your views here.

'''
Function: index()

Description:
This function is django specific. It represents the operations that happen when the url with the same name as the
function is requested. This specific function handles the home page. It handles "post" requests and saves
data to the database which gets displayed to the user.
'''
def index(request):
    rc = RequestContext(request)
    posts = Post.objects.all()
    context = {}

    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.content = post.content.replace(" ","")
            post.key = post.key.replace(" ", "")
            post.content = vigEncrypt(post.content, post.key)
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


'''
Function: index()

Description:
This function is django specific. It represents the operations that happen when the url with the same name as the
function is requested. This specific function handles the decryption page. It handles "post" requests and modifies
data in the database without saving it permanently so that the user can see if their key decrypted any message.
'''
def decrypt(request):
    rc = RequestContext(request)
    posts = Post.objects.all()
    postAry = [p.content for p in posts]
    decryptAry = []
    context = {}

    if request.method == "POST":
        form = KeyForm(data=request.POST)
        if form.is_valid():
            key = form.cleaned_data
            key = key.get("key")
            key = key.replace(" ", "")

            for p in postAry:
                p = vigDecrypt(p, key)
                decryptAry.append(p)
            context['form'] = KeyForm()
            context['posts'] = decryptAry
            response = render_to_response("decrypt.html", context, rc)
            return response
        else:
            pass
    else:
        form = KeyForm()
    context['form'] = form
    context['posts'] = postAry
    response = render_to_response("decrypt.html", context, rc)
    return response



