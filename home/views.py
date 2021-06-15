from django.shortcuts import render
from home.queries import n_customers, n_products, n_employees

# Create your views here.

def home(request):
    print (n_customers(), n_products(), n_employees())
    return render(request, 'home.html', {
        'n_customers':n_customers(),
        'n_products':n_products(),
        'n_employees':n_employees()
    })