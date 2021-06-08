from product.models import Product
from django.shortcuts import render, redirect
from authentification.views import verify_login
from product.queries import retrieve_info, add_product

# Create your views here.
@verify_login
def update_products(request, id):
    if request.method == 'GET':
        product, title, big_title = retrieve_info(id)
        return render(request, 'update_products.html', {'product': product, 'title':title, 'big_title':big_title, 'id':id})
    elif request.method == 'POST':
        product = add_product(request.POST, id)
        return redirect('product', id=product.id)

@verify_login
def product(request, id):
    product, _, _ = retrieve_info(id)
    return render(request, 'product.html', {'product': product})

@verify_login
def all_products(request):
    all_products = list(Product.objects.all().order_by('id'))
    return render(request, 'all_products.html', {'all_products': all_products})