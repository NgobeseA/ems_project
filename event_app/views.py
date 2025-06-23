from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'{user.username}, logged in successfully')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
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

def logout_view(request):
    user = request.user
    logout(request, user)
    return redirect('home')