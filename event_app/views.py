from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import EventForm
from .models import Category, Event

# Create your views here.
def home_view(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

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
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}, your account was created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please check the errors below.')
    else:
        register_form = UserCreationForm()
    return render(request, 'registration.html', {'form': register_form})

def logout_view(request):
    logout(request)
    messages.success('You have logged out successfully')
    return redirect('home')

@login_required
def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)
        print(f"form created with post {request.POST.get('title')}")
        if event_form.is_valid():
            print(f'form is valid indeed')
            event = event_form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Event was created successfully..')
            return redirect('home')
        else:
            print("Nooooo")
            print(event_form.errors)
            messages.error(request, 'Invalid details on the event, Please check the errors')
    else:
        event_form = EventForm()
    
    return render(request, 'create_event.html', {'event_form': event_form})