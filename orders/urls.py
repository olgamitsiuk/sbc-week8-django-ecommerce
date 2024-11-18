from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order-list'),
    path('create/', views.order_create, name='order-create'),
    path('edit/<int:pk>/', views.order_edit, name='order-update'),
    path('delete/<int:pk>/', views.order_delete, name='order-delete'),
]