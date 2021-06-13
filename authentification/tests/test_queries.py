from customer.models import VisitCard, Adress
from authentification.queries import create_or_update_adress, create_user, delete_user, is_already_user, update_user, verify_password
from django.test import TestCase
from authentification.models import User

class QueryTestCase(TestCase):

    def setUp(self):
        user = User(username='usertest', password='passtest', email='mailtest')
        user.save()

    def test_is_already_user(self):
        assert is_already_user(self.user)

    def test_create_user(self):
        user_test = 'usertest'
        infos = {
            'status': 'Em',
            'email': 'test@test.test',
            'job': 'jobtest',
            'username': user_test,
            'password': 'passtest'
        }
        create_user(infos)
        assert is_already_user(user_test)

    def test_verify_password_1(self):
        assert verify_password(self.user.id, 'test_1', 'test_2')

    def test_verify_password_2(self):
        assert not verify_password(self.user.id, 'test', 'test')

    def test_verify_password_3(self):
        assert not verify_password(self.user.id, '', '')

    def test_update_user_1(self):
        test_change = 'anotherstreet'
        adress = Adress(
            street='street',
            number='number',
            city='city',
            state='state',
            country='country',
            postal_code='postal_code'
        )
        adress.save()

        visit_card = VisitCard(
            photo='photo',
            first_name='first_name',
            surname='surname',
            adress=adress,
            email='email'
        )
        visit_card.save()

        user = User(
            email='email',
            password='password',
            username='username',
            visit_card=visit_card
        )
        user.save()
        infos = {
            'street': test_change,
            'number':'number',
            'city':'city',
            'state':'state',
            'country':'country',
            'postal_code':'postal_code',
            'photo':'photo',
            'first_name':'first_name',
            'surname':'surname',
            'email':'email'

        }
        update_user(user, infos)
        assert user.visit_card.adress.street == test_change

    def test_update_user_2(self):
        test_change = 'anotheremail'
        adress = Adress(
            street='street',
            number='number',
            city='city',
            state='state',
            country='country',
            postal_code='postal_code'
        )
        adress.save()

        visit_card = VisitCard(
            photo='photo',
            first_name='first_name',
            surname='surname',
            adress=adress,
            email='email'
        )
        visit_card.save()

        user = User(
            email='email',
            password='password',
            username='username',
            visit_card=visit_card
        )
        user.save()
        infos = {
            'street': 'street',
            'number':'number',
            'city':'city',
            'state':'state',
            'country':'country',
            'postal_code':'postal_code',
            'photo':'photo',
            'first_name':'first_name',
            'surname':'surname',
            'email':test_change

        }
        update_user(user, infos)
        assert user.email == test_change

    def test_create_or_update_adress_1(self):
        adress = None
        data_test = 'city'
        infos = {
            'street': 'street',
            'number':'number',
            'city':data_test,
            'state':'state',
            'country':'country',
            'postal_code':'postal_code',
        }
        adress = create_or_update_adress(adress, infos)
        assert adress.city == data_test

    def test_create_or_update_adress_2(self):
        adress = Adress(
            street='street',
            number='number',
            city='city',
            state='state',
            country='country',
            postal_code='postal_code'
        )
        data_test = 'anothercity'
        infos = {
            'street': 'street',
            'number':'number',
            'city':data_test,
            'state':'state',
            'country':'country',
            'postal_code':'postal_code',
        }
        adress = create_or_update_adress(adress, infos)
        assert adress.city == data_test

    def test_delete_user(self):
        adress = Adress(
            street='street',
            number='number',
            city='city',
            state='state',
            country='country',
            postal_code='postal_code'
        )
        adress.save()

        visit_card = VisitCard(
            photo='photo',
            first_name='first_name',
            surname='surname',
            adress=adress,
            email='email'
        )
        visit_card.save()

        user = User(
            email='email',
            password='password',
            username='username',
            visit_card=visit_card
        )
        user.save()
        delete_user(user.id)
        assert not Adress.objects.filter(id=adress.id).exists()
        assert not VisitCard.objects.filter(id=visit_card.id).exists()
        assert not User.objects.filter(id=user.id).exists()
