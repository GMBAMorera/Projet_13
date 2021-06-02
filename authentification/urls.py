from django.urls import path
from authentification import views

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('register', views.register, name='register'),
    path('account', views.account, name='account')
]