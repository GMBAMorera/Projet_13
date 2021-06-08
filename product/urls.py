from django.urls import path
from customer import views

urlpatterns = [
    path('update_products/<int:pr_id>', views.update_products, name='update_products'),
    path('product/<int:pr_id>', views.product, name='product'),
    path('all_products', views.all_products, name='all_products')
]