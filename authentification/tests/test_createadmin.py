from django.test import TestCase
from authentification.managements.commands import createadmin
from authentification.models import User

class QueryTestCase(TestCase):

    def test_createadmin(self):
        test_user = createadmin.Command().handle(options={'username': 'test_admin', 'password': 'test_admin'})
        assert test_user.password == 'test_password'