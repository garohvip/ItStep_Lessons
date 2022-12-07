from django.urls import path
from two_aapp.views import dictsort, images

urlpatterns = [
    path('books/', images),
]