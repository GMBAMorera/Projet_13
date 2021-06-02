from customer.models import VisitCard
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from authentification.models import User

# Create your views here.

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'incomplete_login': False})
    elif request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            return render(request, 'login.html', {'incomplete_login': True})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'wrong_typed_pw':False, 'exists_already': False})
    elif request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            password = request.POST['password']
        else:
            return render(request, 'register.html', {'wrong_typed_pw':True, 'exists_already': False})
        username = request.POST['username']
        email = request.POST['email']
        status = request.POST['status']
        exists_already = User.objects.filter(username=username).exists()
        if exists_already is True:
            return render(request, 'register.html', {'wrong_typed_pw':False, 'exists_already': True})

        visit_card = VisitCard(company="ocmanager", status=status)
        visit_card.save()

        new_user = User(username=username, password=password, visit_card=visit_card)
        new_user.save()
        return redirect('home')

def account(request):
    return redirect('home')