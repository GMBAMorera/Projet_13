from product.models import Product
from product.queries import add_product, delete, get_or_raise404, save, str_to_float, update, retrieve_info
from django.test import TestCase
from django.http import Http404
from constants import HOME_COMPANY

class QueryTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_or_raise404_1(self):
        product = Product(
            name = 'name',
            off_the_shelf_price = 10,
            production_cost = 5,
            description = 'desc',
            stock = 2,
            stock_unit = 'unit'
        )
        product.save()
        assert get_or_raise404(product.id) == product

    def test_get_or_raise404_2(self):
        self.assertRaises(Http404, get_or_raise404, 22)

    def test_retrieve_info_1(self):
        self.assertIsNone(retrieve_info(0))

    def test_retrieve_info(self):
        product = Product(
            name = 'name',
            off_the_shelf_price = '10',
            production_cost = '5',
            description = 'desc',
            stock = '2',
            stock_unit = 'unit',
            photo = 'test.test'
        )
        product.save()
        assert retrieve_info(product.id) == product

    def test_save(self):
        test = 'desc'
        infos = {
            'name': 'name',
            'off_the_shelf_price': '10',
            'production_cost': '5',
            'description': test,
            'stock': '2',
            'stock_unit': 'unit',
            'photo': 'test.test'
        }
        product = save(infos)
        assert product.description == test

    def test_update(self):
        product = Product(
            name = 'name',
            off_the_shelf_price = '10',
            production_cost = '5',
            description = 'desc',
            stock = '2',
            stock_unit = 'unit',
            photo = 'test.test'
        )
        product.save()
        test = 'anotherdesc'
        infos = {
            'name': 'name',
            'off_the_shelf_price': '10',
            'production_cost': '5',
            'description': test,
            'stock': '2',
            'stock_unit': 'unit',
            'photo': 'test.test'
        }
        product = update(infos, product.id)
        assert product.description == test

    def test_add_product_1(self):
        product = Product(
            name = 'name',
            off_the_shelf_price = '10',
            production_cost = '5',
            description = 'desc',
            stock = '2',
            stock_unit = 'unit',
            photo = 'test.test'
        )
        product.save()
        test = 'anotherdesc'
        infos = {
            'name': 'name',
            'off_the_shelf_price': '10',
            'production_cost': '5',
            'description': test,
            'stock': '2',
            'stock_unit': 'unit',
            'photo': 'test.test'
        }
        product = add_product(infos, product.id)
        assert product.description == test

    def test_add_product_2(self):
        test = 'desc'
        infos = {
            'name': 'name',
            'off_the_shelf_price': '10',
            'production_cost': '5',
            'description': test,
            'stock': '2',
            'stock_unit': 'unit',
            'photo': 'test.test'
        }
        product = add_product(infos, 0)
        assert product.description == test

    def test_str_to_float(self):
        assert str_to_float("50,04") == 50.04

    def test_delete(self):
        product = Product(
            name = 'name',
            off_the_shelf_price = '10',
            production_cost = '5',
            description = 'desc',
            stock = '2',
            stock_unit = 'unit',
            photo = 'test.test'
        )
        product.save()
        delete(product.id)
        assert not Product.objects.filter(id=product.id).exists()