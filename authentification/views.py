from customer.models import Adress, VisitCard
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from authentification.models import User
import functools
from constants import HOME_COMPANY
from django.contrib.auth.hashers import make_password
# Create your views here.


def verify_login(view):
    @functools.wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view(request, *args, **kwargs)
    return wrapper

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'incomplete_login': False})
    elif request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            return render(request, 'login.html', {'incomplete_login': True})

@verify_login
def register(request):
    if request.user.visit_card.status != "Ad":
        return redirect('home')

    if request.method == 'GET':
        return render(request, 'register.html', {'wrong_typed_pw':False, 'exists_already': False})
    elif request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            password = make_password(request.POST['password'])
        else:
            return render(request, 'register.html', {'wrong_typed_pw':True, 'exists_already': False})
        username = request.POST['username']
        email = request.POST['email']
        job = request.POST['job']
        status = request.POST['status']
        exists_already = User.objects.filter(username=username).exists()
        if exists_already is True:
            return render(request, 'register.html', {'wrong_typed_pw':False, 'exists_already': True})

        visit_card = VisitCard(company=HOME_COMPANY, status=status, email=email, job=job)
        visit_card.save()

        new_user = User(username=username, password=password, email=email, visit_card=visit_card)
        new_user.save()
        return redirect('home')

@verify_login
def account(request):
    if request.user.visit_card.surname == '':
        return redirect('update_account')
    else:
        return render(request, 'account.html')

@verify_login
def update_account(request):
    if request.method == 'GET':
        return render(request, 'update_account.html', {'wrong_typed_pw': False})
    elif request.method == 'POST':
        post = request.POST
        photo = post['photo']
        first_name = post['first_name']
        surname = post['surname']
        email=post['email']

        if request.user.visit_card.adress is None:
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
                id=request.user.visit_card.adress.id
            ).update(
                street=post['street'],
                number=post['number'],
                city=post['city'],
                state=post['state'],
                country=post['country'],
                postal_code=post['postal_code']
            )
            adress = request.user.visit_card.adress

        new_password = post['password']
        if new_password != '':
            if new_password == post['password2']:
                User.objects.filter(
                    id=request.user.id
                ).update(
                    password=new_password
                )
            else:
                return render(request, 'update_account.html', {'wrong_typed_pw': True})

        VisitCard.objects.filter(
            id=request.user.visit_card.id
        ).update(
            photo=photo,
            first_name=first_name,
            surname=surname,
            adress=adress,
            email=email
        )

        User.objects.filter(
            id=request.user.id
        ).update(
            email=email
        )

        return redirect('account')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

@verify_login
def all_employees(request):
    employees = list(VisitCard.objects.filter(status='Em').order_by('id'))
    print(employees)
    return render(request, 'all_employees.html', {'employees': employees})