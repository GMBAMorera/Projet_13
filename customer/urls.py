from django.urls import path
from customer import views

urlpatterns = [
    path('update_customers/<int:vc_id>', views.update_customers, name='update_customers'),
    path('customer/<int:vc_id>', views.customer, name='customer'),
    path('all_customers', views.all_customers, name='all_customers')
]