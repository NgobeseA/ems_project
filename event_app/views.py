from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import EventForm, LoginForm, RegisterForm, EventFilterForm
from .models import Category, Event

# Create your views here.
def home_view(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

def gallery_views(request):
    return render(request, 'gallery.html')

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)

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
        login_form = LoginForm()
    return render(request, 'login.html', {'form': login_form})

def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}, your account was created successfully!')
            return redirect('home')
        else:
            messages.error(request, f'Registration failed. Please check the errors below. {register_form.errors}')
    else:
        register_form = RegisterForm()
    return render(request, 'registration.html', {'form': register_form})

def logout_view(request):
    logout(request)
    messages.success('You have logged out successfully')
    return redirect('home')

@login_required(login_url='login')
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

def view_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_details.html', {'event': event})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event and request.user == event.organizer:
        if request.method == 'POST':
            title = event.title
            event.delete()
            messages.success(request, f'Successfully deleted {title}')
            return redirect('home')
    else:
        messages.warning(request, "Only an orginizer can perform this action.")
    
    return render(request, 'event_details.html', {'event': event})

@login_required(login_url='login')
def edit_event_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event and request.user != event.organizer:
        messages(request, "Only an orginizer can perfom this action.")
        return redirect('home')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully')
            return redirect('view_event', pk=event.pk)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        event_form = EventForm(instance=event)
    return render(request, 'create_event.html', {'event_form': event_form})

def event_list_view(request):
    form = EventFilterForm(request.GET or None)

    form.fields['location'].choices = [('', 'All locations')] + list(Event.objects.values_list('location', 'location').distinct())
    form.fields['category'].choices = [('', 'All categories')] + list(Event.objects.values_list('category', 'category').distinct())


    events = Event.objects.all()

    if form.is_valid():
        search = form.cleaned_data.get('search')
        location = form.cleaned_data.get('location')
        category = form.cleaned_data.get('category')
        date_range = form.cleaned_data.get('date_range')

        if search:
            pass

    return render(request, 'event_list.html', {'form': form, 'events': events})

def get_started_view(request):
    if request.method == 'POST':
        pass

@login_required(login_url='login')
def users_events(request):
    user = request.user
    try:
        my_events = Event.objects.filter(organizer=user)
    except:
        my_events = None

    return render(request, 'my_events.html', {'events': my_events})