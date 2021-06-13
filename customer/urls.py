from django.urls import path
from customer import views

urlpatterns = [
    path('update_customers/<int:id>', views.update_customers, name='update_customers'),
    path('customer/<int:id>', views.customer, name='customer'),
    path('all_customers', views.all_customers, name='all_customers'),
    path('delete_customer/<int:id>', views.delete_customer, name='delete_customer')
]