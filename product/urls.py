from django.urls import path
from product import views

urlpatterns = [
    path('update_products/<int:id>', views.update_products, name='update_products'),
    path('product/<int:id>', views.product, name='product'),
    path('all_products', views.all_products, name='all_products'),
    path('delete_product/<int:id>', views.delete_product, name="delete_product")
]