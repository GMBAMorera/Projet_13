from django.urls import path
from authentification import views

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('register', views.register, name='register'),
    path('account', views.account, name='account'),
    path('logout', views.logout_page, name='logout'),
    path('update_account', views.update_account, name='update_account'),
    path('all_employees', views.all_employees, name='all_employees')
]