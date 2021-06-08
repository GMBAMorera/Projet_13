from django.http.response import Http404
from product.models import Product
from django.http import Http404

def retrieve_info(id):
    if id == 0:
        return None, "Add Product", "Ajouter un nouveau Produit"
    else:
        try:
            product = Product.objects.get(id=id)
            return product, "Update", "Modifier un Produit"
        except Product.DoesNotExist:
            raise Http404("Ce produit n'existe pas.")

def add_product(infos, id):
    if id == 0:
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

    else:
        Product.objects.filter(id=id).update(
            name = infos["name"],
            off_the_shelf_price = str_to_float(infos["off_the_shelf_price"]),
            production_cost = str_to_float(infos["production_cost"]),
            description = infos["description"],
            stock = str_to_float(infos["stock"]),
            stock_unit = infos["stock_unit"],
            photo = infos["photo"]
        )
        product = Product.objects.get(id=id)

    return product

def str_to_float(number):
    return float(number.replace(",", "."))