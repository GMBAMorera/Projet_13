from django.contrib.auth.hashers import make_password

from customer.models import Adress, VisitCard
from authentification.models import User
from constants import HOME_COMPANY


def is_already_user(username):
    return User.objects.filter(username=username).exists()

def create_user(infos):
    visit_card = VisitCard(
        company=HOME_COMPANY,
        status=infos['status'],
        email=infos['email'],
        job=infos['job']
    )
    visit_card.save()

    new_user = User(
        username=infos['username'],
        password=make_password(infos['password']),
        email=visit_card.email,
        visit_card=visit_card
    )
    new_user.save()

def verify_password(user_id, password1, password2):
    if password1 != password2:
        return True
    elif password1 != '':
        User.objects.filter(
            id=user_id
        ).update(
            password=make_password(password1)
        )
    return False

def update_user(user, infos):
    adress = create_or_update_adress(user.visit_card.adress, infos)
    VisitCard.objects.filter(
        id=user.visit_card.id
    ).update(
        photo=infos['photo'],
        first_name=infos['first_name'],
        surname=infos['surname'],
        adress=adress,
        email=infos['email']
    )

    User.objects.filter(
        id=user.id
    ).update(
        email=infos['email']
    )

def create_or_update_adress(adress, post):
    if adress is None:
        adress = Adress(
            street=post['street'],
            number=post['number'],
            city=post['city'],
            state=post['state'],
            country=post['country'],
            postal_code=post['postal_code']
        )
        adress.save()
    else:
        Adress.objects.filter(
            id=adress.id
        ).update(
            street=post['street'],
            number=post['number'],
            city=post['city'],
            state=post['state'],
            country=post['country'],
            postal_code=post['postal_code']
        )
    return adress

def employees_list():
    return list(User.objects.all().order_by('id'))

def delete_user(id):
    user = User.objects.get(id=id)
    visit_card = user.visit_card
    adress = visit_card.adress
    user.delete()
    visit_card.delete()
    adress.delete()