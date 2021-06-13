from customer.models import PersonnalWebAdress, VisitCard, Adress, WebAdress
from customer.queries import add_visit_card, create_visit_card, delete_visit_card, get_visit_card_or_404, retrieve_info, retrieve_visit_card, retrieve_web_adress, update_visit_card
from django.test import TestCase
from django.http import Http404
from constants import HOME_COMPANY

class QueryTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_visit_card_or_404_1(self):
        visit_card = VisitCard(
            company=HOME_COMPANY,
            status = 'Em'
        )
        visit_card.save()
        assert get_visit_card_or_404(id=visit_card.id) == visit_card
    
    def test_get_visit_card_404_2(self):
        self.assertRaises(Http404, get_visit_card_or_404, 22)

    def test_retrieve_visit_card_1(self):
        self.assertIsNone(retrieve_visit_card(0))

    def test_retrieve_visit_card_2(self):
        visit_card = VisitCard(
            company=HOME_COMPANY,
            status = 'Em'
        )
        visit_card.save()
        assert get_visit_card_or_404(id=visit_card.id) == visit_card

    def test_retrieve_web_adress(self):
        visit_card = VisitCard(
            company=HOME_COMPANY,
            status = 'Em'
        )
        visit_card.save()
        web_adress = WebAdress(
            web_adress='test.com',
            site_name='test'
        )
        web_adress.save()
        pwa = PersonnalWebAdress(
            web_adress=web_adress,
            visit_card=visit_card
        )
        pwa.save()
        assert retrieve_web_adress(visit_card) == web_adress

    def test_retrieve_info(self):
        visit_card = VisitCard(
            company=HOME_COMPANY,
            status = 'Em'
        )
        visit_card.save()
        web_adress = WebAdress(
            web_adress='test.com',
            site_name='test'
        )
        web_adress.save()
        pwa = PersonnalWebAdress(
            web_adress=web_adress,
            visit_card=visit_card
        )
        pwa.save()
        assert retrieve_info(visit_card.id) == (visit_card, web_adress)

    def test_create_visit_card(self):
        test = "photo"
        infos = {
            'street':"street",
            'number':"number",
            'city':"city",
            'state':"state",
            'country':"country",
            'postal_code':"postal_code",
            'company':"company",
            'job':"job",
            'photo':test,
            'first_name':"first_name",
            'surname':"surname",
            'email':"email",
            'status':'Em',
            'web_adress':"web_adress",
            'site_name':"site_name"
        }
        visit_card = create_visit_card(infos)
        assert visit_card.photo == test
        assert PersonnalWebAdress.objects.filter(visit_card=visit_card).exists()

    def test_update_visit_card(self):
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
            company=HOME_COMPANY,
            status = 'Em',
            adress=adress
        )
        visit_card.save()
        web_adress = WebAdress(
            web_adress='test.com',
            site_name='test'
        )
        web_adress.save()
        pwa = PersonnalWebAdress(
            web_adress=web_adress,
            visit_card=visit_card
        )
        pwa.save()
        test = "another_first_name"
        infos = {
            'street':"street",
            'number':"number",
            'city':"city",
            'state':"state",
            'country':"country",
            'postal_code':"postal_code",
            'company':"company",
            'job':"job",
            'photo':'photo',
            'first_name': test,
            'surname':"surname",
            'email':"email",
            'status':'Em',
            'web_adress':"web_adress",
            'site_name':"site_name"
        }
        visit_card = update_visit_card(infos, visit_card.id)
        print("first name_out: ", visit_card.first_name)
        assert test in visit_card.first_name

    def test_add_visit_card_1(self):
        test = "photo"
        infos = {
            'street':"street",
            'number':"number",
            'city':"city",
            'state':"state",
            'country':"country",
            'postal_code':"postal_code",
            'company':"company",
            'job':"job",
            'photo':test,
            'first_name':"first_name",
            'surname':"surname",
            'email':"email",
            'status':'Em',
            'web_adress':"web_adress",
            'site_name':"site_name"
        }
        visit_card = add_visit_card(infos, 0)
        assert visit_card.photo == test
        assert PersonnalWebAdress.objects.filter(visit_card=visit_card).exists()

    def test_add_visit_card(self):
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
            company=HOME_COMPANY,
            status = 'Em',
            adress=adress
        )
        visit_card.save()
        web_adress = WebAdress(
            web_adress='test.com',
            site_name='test'
        )
        web_adress.save()
        pwa = PersonnalWebAdress(
            web_adress=web_adress,
            visit_card=visit_card
        )
        pwa.save()
        test = "another_first_name"
        infos = {
            'street':"street",
            'number':"number",
            'city':"city",
            'state':"state",
            'country':"country",
            'postal_code':"postal_code",
            'company':"company",
            'job':"job",
            'photo':'photo',
            'first_name': test,
            'surname':"surname",
            'email':"email",
            'status':'Em',
            'web_adress':"web_adress",
            'site_name':"site_name"
        }
        visit_card = add_visit_card(infos, visit_card.id)
        assert visit_card.first_name == test

    def test_delete_visit_card(self):
        infos = {
            'street':"street",
            'number':"number",
            'city':"city",
            'state':"state",
            'country':"country",
            'postal_code':"postal_code",
            'company':"company",
            'job':"job",
            'photo':"photo",
            'first_name':"first_name",
            'surname':"surname",
            'email':"email",
            'status':'Em',
            'web_adress':"web_adress",
            'site_name':"site_name"
        }
        visit_card = create_visit_card(infos)
        adress = visit_card.adress
        web_adress = retrieve_web_adress(visit_card)
        delete_visit_card(visit_card.id)
        assert not Adress.objects.filter(id=adress.id).exists()
        assert not WebAdress.objects.filter(id=web_adress.id).exists()
        assert not VisitCard.objects.filter(id=visit_card.id).exists()
