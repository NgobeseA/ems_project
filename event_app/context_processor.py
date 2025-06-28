from .forms import LoginForm, RegisterForm

def authentication_forms(request):
    return {
        'login_form': LoginForm(),
        'register_form': RegisterForm(), 
    }