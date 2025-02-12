from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticació de l'usuari
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context['error'] = "Usuari o contrasenya incorrectes."
    return render(request, 'authentication/login.html', context)

def index(request):
    context = {
        'message': 'Benvingut a la pàgina d''inici!'
    }
    return render(request, 'authentication/index.html', context)