from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^add-quote$', views.add_quote),
    url(r'^like$', views.like),
    url(r'^delete$', views.delete),
    url(r'^user$', views.user),
    url(r'^edit$', views.edit),
    url(r'^update$', views.update),
    url(r'^logout$', views.logout)
]