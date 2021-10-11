from django.shortcuts import render
from django.http import request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from resume.form import Resumeform
from vacancy.form import Vacancyform

# Create your views here.
class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signup.html'

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'menu/login.html'

def home(request):
    context={
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username
        }
    return render(request, 'menu/home.html', context=context)

def homepage(request):
    form = Vacancyform() if request.user.is_staff else Resumeform()
    context = {
        'form': form,
        'is_authenticated': request.user.is_authenticated,
        'is_staff': request.user.is_staff,
        'username': request.user.username
    }
    return render(request, 'menu/index.html', context=context)