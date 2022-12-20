from django.urls import path
from game_app.views import upload_data

urlpatterns = [
    path('', upload_data),
]
