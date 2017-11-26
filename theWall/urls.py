from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'WallOfSecrets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
    url(r'^decrypt/$', views.decrypt, name="decrypt")
]
