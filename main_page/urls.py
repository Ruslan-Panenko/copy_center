from django.urls import path
from main_page import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('services/', views.service_list, name='service_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('orders/', views.orders, name='orders'),

]
