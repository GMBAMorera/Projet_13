from django.http.response import Http404
from product.models import Product
from django.http import Http404

def get_or_raise404(id):
    try:
        product = Product.objects.get(id=id)
        return product
    except Product.DoesNotExist:
        raise Http404("Ce produit n'existe pas.")

def retrieve_info(id):
    if id == 0:
        return None
    else:
        return get_or_raise404(id)


def save(infos):
    product = Product(
        name = infos["name"],
        off_the_shelf_price = str_to_float(infos["off_the_shelf_price"]),
        production_cost = str_to_float(infos["production_cost"]),
        description = infos["description"],
        stock = str_to_float(infos["stock"]),
        stock_unit = infos["stock_unit"],
        photo = infos["photo"]
    )
    product.save()
    return product

def update(infos, id):
    Product.objects.filter(id=id).update(
        name = infos["name"],
        off_the_shelf_price = str_to_float(infos["off_the_shelf_price"]),
        production_cost = str_to_float(infos["production_cost"]),
        description = infos["description"],
        stock = str_to_float(infos["stock"]),
        stock_unit = infos["stock_unit"],
        photo = infos["photo"]
    )
    return Product.objects.get(id=id)

def add_product(infos, id):
    if id == 0:
        return save(infos)
    else:
        return update(infos, id)

def str_to_float(number):
    return float(number.replace(",", "."))

def delete(id):
    product = retrieve_info(id)
    product.delete()