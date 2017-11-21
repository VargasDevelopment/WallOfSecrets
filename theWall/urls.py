from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'WallOfSecrets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
]
