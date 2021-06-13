
from customer.models import VisitCard
from customer.queries import delete_visit_card, retrieve_visit_card
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from authentification.queries import is_already_user, create_user, verify_password, update_user, employees_list, delete_user
from constants import STATUS_DICT

import functools
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
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
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
        return _register_and_render(request, request.POST)

def _register_and_render(request, infos):
    if infos['password'] != infos['password2']:
        return render(request, 'register.html', {'wrong_typed_pw':True, 'exists_already': False})
    elif is_already_user(infos['username']):
        return render(request, 'register.html', {'wrong_typed_pw':False, 'exists_already': True})
    else:
        create_user(infos)
        return redirect('all_employees')

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

        if verify_password(request.user.id, post['password'], post['password2']):
            return render(request, 'update_account.html', {'wrong_typed_pw': True})

        update_user(request.user, post)

        return redirect('account')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

@verify_login
def all_employees(request):
    employees = employees_list()
    print(employees)
    return render(
        request,
        'all_employees.html',
        {'employees': [(
            employee, 
            STATUS_DICT[employee.visit_card.status]
            ) for employee in employees]
        }
    )

@verify_login
def delete_employee(request, id):
    delete_user(id)    
    return redirect('all_employees')
