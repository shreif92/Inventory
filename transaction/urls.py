from django.urls import path
from .views import *



urlpatterns = [
    path('create_supplier/',CreateSupplier.as_view(),name='create_supplier'),
    path('supplier_list/',SupplierList.as_view(),name='supplier_list'),
    path('update_supplier/<uuid:pk>/',UpdateSupplier.as_view(),name='update_supplier'),
    path('delete_supplier/<uuid:pk>/',DeleteSupplier.as_view(),name='delete_supplier'),
]