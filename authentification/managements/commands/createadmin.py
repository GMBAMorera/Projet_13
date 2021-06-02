from django.core.management.base import BaseCommand, CommandError
from authentification.models import User
from customer.models import VisitCard


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('username', default='admin')
        parser.add_argument('password', default='admin')

    def handle(self, *args, **options):
        visit_card = VisitCard(company='ocmanager', status='admin')
        visit_card.save()

        user = User(username=options['username'], password=options['password'], visit_card=visit_card)
        user.save()
        print("admin created")
        return user