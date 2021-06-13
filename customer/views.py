from customer.models import VisitCard
from django.shortcuts import render, redirect
from authentification.views import verify_login
from customer.queries import retrieve_info, retrieve_web_adress, add_visit_card, delete_visit_card

# Create your views here.
@verify_login
def update_customers(request, id):
    if request.method == 'GET':
        visit_card, web_adress = retrieve_info(id)
        title, big_title = choose_title(id)
        return render(request, 'update_customers.html', {'visit_card': visit_card, 'web_adress': web_adress, 'title':title, 'big_title':big_title, 'id':id})
    elif request.method == 'POST':
        visit_card = add_visit_card(request.POST, id)
        return redirect('customer', id=visit_card.id)

def choose_title(id):
    if id == 0:
        return "Add Customer", "Ajouter un nouveau Client"
    else:
        return "Update", "Modifier une Carte de Visite"

@verify_login
def customer(request, id):
    visit_card, web_adress = retrieve_info(id)
    return render(request, 'customer.html', {'visit_card': visit_card, 'web_adress':web_adress})

@verify_login
def all_customers(request):
    customer_page = list(VisitCard.objects.filter(status='Cu').order_by('id'))
    return render(request, 'all_customers.html', {'customer_page': customer_page})

def delete_customer(request, id):
    delete_visit_card
    return redirect('all_customers')