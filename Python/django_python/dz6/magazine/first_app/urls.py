from django.urls import path
from first_app.views import books, books_year

urlpatterns = [
    path('books/', books),
    path('books/<str:flag>', books_year),
    # path('books/<str:categorie>', books_filter),
]
