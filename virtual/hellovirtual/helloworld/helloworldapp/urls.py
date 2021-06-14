from django.urls import path, include
from .views import hellofunction

urlpatterns = [
    path('world/', hellofunction),
]
