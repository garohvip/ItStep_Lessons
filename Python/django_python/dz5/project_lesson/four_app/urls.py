from django.urls import path
from four_app.views import images

urlpatterns = [
    path('exam/', images)
]