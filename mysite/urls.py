from django.conf.urls import patterns, include, url
from mysite.views import welcome, home, post, login, logout

urlpatterns = patterns('',
    url(r'^$', welcome),
    url(r'^home/$', home),
    url(r'^post/$', post),
    url(r'^login/$',login),
    url(r'^logout/$',logout),
)
