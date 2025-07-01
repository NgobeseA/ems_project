from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
            'class': 'form-control',
            'placeholder': 'Username',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'required',
            'minlength': '8',
            'placeholder': 'Enter password'
        })
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': 'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email','required': 'required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','required': 'required','minlength': '8','placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','required': 'required','minlength': '8','placeholder': 'Confirm password'}))

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
