from authentification.models import User
from customer.models import VisitCard
from product.models import Product

from constants import INV_STATUS_DICT


def n_customers():
    return VisitCard.objects.filter(status=INV_STATUS_DICT['customer']).count()

def n_products():
    return Product.objects.all().count()

def n_employees():
    return User.objects.all().count()