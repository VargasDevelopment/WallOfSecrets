from django.conf.urls import url
from . import views


'''
This file tells django which urls are valid and what to return when a user navigates to each url.
It uses regular expressions to match a URL pattern. I do not take full advantage of the usefulness of 
regular expressions here because the site is too simple to need to create complex URLs
'''
urlpatterns = [
    # Examples:
    # url(r'^$', 'WallOfSecrets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
    url(r'^decrypt/$', views.decrypt, name="decrypt")
]
