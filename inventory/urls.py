from django.urls import path
from .views import *



urlpatterns = [
    path('stock_list',StocklistView.as_view(),name='stock_list'),
    path('create_stock',CreateStock.as_view(),name='create_stock'),
    path('update_stock/<uuid:pk>/',UpdateStock.as_view(),name='update_stock'),
    path('delete_stock/<uuid:pk>/',DeleteStock.as_view(),name='delete_stock'),
]