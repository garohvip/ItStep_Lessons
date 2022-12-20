from django.urls import path
from product_app.views import upload_json

urlpatterns = [
    path('', upload_json),
]
