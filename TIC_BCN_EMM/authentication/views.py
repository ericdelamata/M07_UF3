from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuari  # Assegura't que el teu model es diu així
from .forms import LoginForm

# Login sense sessions: no es guarda cap informació a la sessió
def login_without_session(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                # Comprovem si existeix l'usuari amb les credencials proporcionades
                usuari = Usuari.objects.get(username=username, password=password)
                # Redirigim a la pàgina d'inici
                return redirect('home_without_session')
            except Usuari.DoesNotExist:
                messages.error(request, "Credencials incorrectes")
    else:
        form = LoginForm()
    return render(request, 'login_without_session.html', {'form': form})

def home_without_session(request):
    # Aquesta vista no comprova la sessió, per tant si l'usuari torna al login, haurà d'iniciar sessió de nou.
    return render(request, 'home_without_session.html')


# Login amb sessions: es guarda la informació de l'usuari a la sessió
def login_with_session(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                usuari = Usuari.objects.get(username=username, password=password)
                # Guardem la id de l'usuari a la sessió
                request.session['user_id'] = usuari.id
                return redirect('home_with_session')
            except Usuari.DoesNotExist:
                messages.error(request, "Credencials incorrectes")
    else:
        form = LoginForm()
    return render(request, 'login_with_session.html', {'form': form})

def home_with_session(request):
    # Comprovem que l'usuari ha iniciat sessió
    if 'user_id' in request.session:
        try:
            usuari = Usuari.objects.get(id=request.session['user_id'])
        except Usuari.DoesNotExist:
            # Si no trobem l'usuari, redirigim al login
            return redirect('login_with_session')
        return render(request, 'home_with_session.html', {'user': usuari})
    else:
        return redirect('login_with_session')

def logout_view(request):
    # Esborrem la informació de la sessió
    request.session.pop('user_id', None)
    return redirect('login_with_session')