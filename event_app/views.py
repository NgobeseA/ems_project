from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request, login_form)
            login(request, user)
            return redirect('home')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'form': login_form})

def register_view(request):
    '''
        Create a user account for people who are responsible to post events
    '''
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('home')
    else:
        register_form = UserCreationForm()
    return render(request, 'registration.html', {'form': register_form})

