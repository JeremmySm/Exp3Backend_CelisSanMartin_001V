from django.urls import path
from .views import index, index3, index4, index2, index5

urlpatterns = [
    path('', index, name="index")
    ,path('index3', index3, name="index3"),path('index', index, name="index")
    ,path('index4', index4, name="index4"),path('index', index, name="index")
    ,path('index2', index2, name="index2"),path('index', index, name="index")
    ,path('index5/<id>', index5, name="index5"),path('index', index, name="index")

]
