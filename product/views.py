from authentification.queries import verify_password
from product.models import Product
from django.shortcuts import render, redirect
from authentification.views import verify_login
from product.queries import retrieve_info, add_product, delete

# Create your views here.
@verify_login
def update_products(request, id):
    if request.method == 'GET':
        product = retrieve_info(id)
        title, big_title = choose_title(id)
        return render(request, 'update_products.html', {'product': product, 'title':title, 'big_title':big_title, 'id':id})
    elif request.method == 'POST':
        product = add_product(request.POST, id)
        return redirect('product', id=product.id)

def choose_title(id):
    if id == 0:
        return "Add Product", "Ajouter un nouveau Produit"
    else:
        return "Update", "Modifier un Produit"

@verify_login
def product(request, id):
    product = retrieve_info(id)
    return render(request, 'product.html', {'product': product})

@verify_login
def all_products(request):
    all_products = list(Product.objects.all().order_by('id'))
    return render(request, 'all_products.html', {'all_products': all_products})

@verify_login
def delete_product(request, id):
    delete(id)
    return redirect('home')