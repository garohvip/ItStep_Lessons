from django.urls import path
from first_app.views import books

urlpatterns = [
    path('books/', books)
]