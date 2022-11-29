from django.contrib import admin
from django.urls import path, re_path, include
from first_app.views import *

urlpatterns = [
    path('', home_page),
    # re_path(r'^facts/(?P<info>\w*)?/?$', facts),
    # re_path(r'^contacts/(?P<who>\w*)?/?$', contacts),
    re_path(r'^writes/(?P<write>\w*)?/?$', writes),
    re_path(r'^books/(?P<book>\w*)?/?$', books),
    # re_path(r'^gosduma/(?P<who>\w*)?/?$', gosduma),
    # re_path(r'^history/(?P<info>\w*)?/?$', history),
    # re_path(r'^history/(?P<cities>\w*)?/(?P<info>\w*)?/?$', history_cities),
]
