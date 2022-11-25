from django.contrib import admin
from django.urls import path, re_path, include
from first_app.views import *

urlpatterns = [
    path('', home_page),
    # path('news/', news),
    # path('management/', management),
    path('faq/', faq),
    path('contact/', contact),
    # re_path(r'news/\w*/', news),
    # re_path(r'management/\w*/', management),
    re_path(r'faq/\w*/', faq),
    re_path(r'contact/\w*/', contact),
    re_path(r'^news/(?P<city>\w*)?/?$', news),
    re_path(r'^management/(?P<who>\w*)?/?$', management),
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