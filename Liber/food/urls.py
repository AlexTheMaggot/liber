from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('<slug:slug_restaurant>/', views.dish_list, name='dish_list'),
    path('<slug:slug_restaurant>/add', views.dish_list, name='dish_add'),
    path('<slug:slug_restaurant>/<slug:slug_dish>/', views.dish_detail, name='dish_detail')
]