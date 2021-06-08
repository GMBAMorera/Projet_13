from customer.models import VisitCard
from django.shortcuts import render, redirect
from authentification.views import verify_login
from customer.queries import retrieve_info, retrieve_web_adress, add_visit_card

# Create your views here.
@verify_login
def update_customers(request, vc_id):
    if request.method == 'GET':
        visit_card, title, big_title = retrieve_info(vc_id)
        return render(request, 'update_customers.html', {'visit_card': visit_card, 'title':title, 'big_title':big_title, 'vc_id':vc_id})
    elif request.method == 'POST':
        visit_card = add_visit_card(request.POST, vc_id)
        return redirect('customer', vc_id=visit_card.id)

@verify_login
def customer(request, vc_id):
    visit_card, _, _ = retrieve_info(vc_id)
    web_adress = retrieve_web_adress(visit_card)
    return render(request, 'customer.html', {'visit_card': visit_card, 'web_adress':web_adress})

@verify_login
def all_customers(request):
    customer_page = list(VisitCard.objects.filter(status='Cu').order_by('id'))
    return render(request, 'all_customers.html', {'customer_page': customer_page})