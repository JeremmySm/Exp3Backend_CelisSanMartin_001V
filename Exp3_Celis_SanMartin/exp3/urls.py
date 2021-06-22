from django.urls import path
from .views import index, index3

urlpatterns = [
    path('', index, name="index")
    ,path('index3', index3, name="index3"),path('index', index, name="index")
]
