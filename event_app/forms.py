from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','image', 'brief', 'category', 'date','start_time', 'end_time', 'location', 'venue', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'brief': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control form-select'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-field',
            'placeholder': 'Username',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'required': 'required',
            'minlength': '8',
            'placeholder': 'Enter password'
        })
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    mobile_number = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class RegisterForm(UserCreationForm):
        username = forms.CharField()
        email = forms.EmailField()
        mobile_number = forms.CharField()
        password1 = forms.CharField()
        password2 = forms.CharField()

        class Meta:
            model = User  # Note the colon before the User class
            fields = ['username', 'email', 'mobile_number', 'password1', 'password2']

class EventFilterForm(forms.Form):
    search_input = forms.CharField(label="Search Event", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search events...'}))
    location = forms.ChoiceField(choices=[],required=False,widget=forms.Select(attrs={'class':'form-select'}))
    category = forms.ChoiceField(choices=[], required=False,widget=forms.Select(attrs={'class': 'form-select'}))
    date_range = forms.ChoiceField(
        label="Date", 
        required=False, 
        choices=[
            ('','Any date'), 
            ('today', 'Today'), 
            ('week', 'Next 7 Days'), 
            ('month', 'Next 30 Days'),
        ],
        widget=forms.Select(
            attrs={'class':'form-select'}
        )
    )
