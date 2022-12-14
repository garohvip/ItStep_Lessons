from django.contrib import admin
from django.urls import path, re_path, include
from first_app.views import *

urlpatterns = [
    path('', home_page),
    # path('news/', news),
    # path('management/', management),
    # path('faq/', faq),
    # path('contact/', contact),
    # re_path(r'news/\w*/', news),
    # re_path(r'management/\w*/', management),
    # re_path(r'^faq/(?P<info>\w*)?/?$', faq),
    # re_path(r'^contact/(?P<who>\w*)?/?$', contact),
    # re_path(r'^news/(?P<city>\w*)?/?$', news),
    # re_path(r'^management/(?P<who>\w*)?/?$', management),
    re_path(r'^facts/(?P<info>\w*)?/?$', facts),
    re_path(r'^contacts/(?P<who>\w*)?/?$', contacts),
    re_path(r'^news/(?P<where>\w*)?/?$', news),
    re_path(r'^gosduma/(?P<who>\w*)?/?$', gosduma),
    re_path(r'^history/(?P<info>\w*)?/?$', history),
    re_path(r'^history/(?P<cities>\w*)?/(?P<info>\w*)?/?$', history_cities),
    # path('<str:table_sql>/', check_views),
    # path('<str:table_sql>/add=<str:nameProduct>/', add_views),
    # path('<str:table_sql>/del=<str:nameProduct>/', del_views),
    # re_path(r'^years/(?P<year>19[1-9]\d)?/$', year_old),
    # re_path(r'^number/(?P<number>\+380\d{9})?/$', number_phone),
    # re_path(r'^mail/(?P<mail>([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6})?/$', mail_post),
    # path('second3/<int:number1> <int:number2>/', second_views_three),
    # path('second4/<str:table_sql>/', second_views_four),
    # path('second5/<str:table_sql>/', second_views_five_json),
    # path('second/<str:table_sql>/', second_views),
    # path('second/<str:table_sql>/', second_views)
]
