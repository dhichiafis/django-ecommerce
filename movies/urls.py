from django.urls import path 
from .views import *
urlpatterns=[
 path('movies/',movies_list,name='movies_list'),
 path('<int:id>/',movie_detail,name='movies/movies_detail'),
 path('<int:id>/add/',add_to_cart,name='add_to_cart'),
 path('/cart/',cart_detail,name='cart_detail'),
 path('/clear',clear_cart,name='clear_cart'),
 path('/purchase',purchase,name='purchase')
]