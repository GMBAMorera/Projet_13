from django.http.response import Http404
from customer.models import VisitCard, Adress, WebAdress, PersonnalWebAdress
from django.http import Http404

def get_visit_card_or_404(id):
    try:
        return VisitCard.objects.get(id=id)
    except VisitCard.DoesNotExist:
        raise Http404("Ce client n'existe pas.")

def retrieve_visit_card(id):
    if id == 0:
        return None
    else:
        return get_visit_card_or_404(id)

def retrieve_web_adress(visit_card):
    if visit_card is None:
        return None
    else:
        return PersonnalWebAdress.objects.get(visit_card=visit_card).web_adress

def retrieve_info(id):
    visit_card = retrieve_visit_card(id)
    web_adress = retrieve_web_adress(visit_card)
    return visit_card, web_adress

def add_visit_card(infos, id):
    if id == 0:
        return create_visit_card(infos)
    else:
        return update_visit_card(infos, id)

def create_visit_card(infos):
    adress = Adress(
        street=infos["street"],
        number=infos["number"],
        city=infos["city"],
        state=infos["state"],
        country=infos["country"],
        postal_code=infos["postal_code"]
    )
    
    visit_card = VisitCard(
        company=infos["company"],
        job=infos["job"],
        photo=infos["photo"],
        first_name=infos["first_name"],
        surname=infos["surname"],
        email=infos["email"],
        adress=adress,
        status=infos["status"]
    )
    
    web_adress = WebAdress(
        web_adress=infos["web_adress"],
        site_name=infos["site_name"]
    )

    personnal_web_adress = PersonnalWebAdress(
        web_adress=web_adress,
        visit_card=visit_card
    )

    adress.save()
    visit_card.save()
    web_adress.save()
    personnal_web_adress.save()
    return visit_card

def update_visit_card(infos, id):
    visit_card = VisitCard.objects.get(id=id)
    VisitCard.objects.filter(id=visit_card.id).update(
        company=infos["company"],
        job=infos["job"],
        photo=infos["photo"],
        first_name=infos["first_name"],
        surname=infos["surname"],
        email=infos["email"],
        status=infos["status"]
    )

    adress = visit_card.adress
    Adress.objects.filter(id=adress.id).update(
        street=infos["street"],
        number=infos["number"],
        city=infos["city"],
        state=infos["state"],
        country=infos["country"],
        postal_code=infos["postal_code"]
    )

    personnal_web_adress = PersonnalWebAdress.objects.get(visit_card=visit_card)
    web_adress = personnal_web_adress.web_adress
    WebAdress.objects.filter(id=web_adress.id).update(
        web_adress=infos["web_adress"],
        site_name=infos["site_name"]
    )

    return VisitCard.objects.get(id=id)

def add_visit_card(infos, id):
    if id == 0:
        return create_visit_card(infos)
    else:
        return update_visit_card(infos, id)

def delete_visit_card(id):
    visit_card, web_adress = retrieve_info(id)
    adress = visit_card.adress

    web_adress.delete()
    visit_card.delete()
    adress.delete()