from django.urls import path,include
from container_dealer_portal.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$',index),
    url(r'^login/$',login),
    url(r'^auth/$',auth_view),
    url(r'^logout/$',logout_view),
    url(r'^register/$',register),
    url(r'^registration/$',registration),
    url(r'^add_container/$', add_container),
    url(r'^manage_vehicles/$',manage_vehicles),
    url(r'^order_list/$',order_list),
    url(r'^complete/$',complete),
    url(r'^history/$',history),
    url(r'^delete/$',delete),
    url(r'^webadmin/$', webadmin),
]
