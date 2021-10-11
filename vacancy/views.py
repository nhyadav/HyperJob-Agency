from django.shortcuts import render, redirect
from django.http import request, HttpResponseForbidden
from .models import Vacancy
from.form import Vacancyform
from django.core.exceptions import PermissionDenied
# Create your views here.
def vacancy(request):
    vacancy = Vacancy.objects.all()
    return render(request, "vacancy/vacancy.html", {'vacancy': vacancy})

def new_vacancy(request):
    if request.method == 'POST':
        can_submit = request.user.is_authenticated and request.user.is_staff
        if not can_submit:
            # raise PermissionDenied
            return HttpResponseForbidden(status=403)
        
        form = Vacancyform(request.POST)
        if not form.is_valid():
            return HttpResponseForbidden(status=403)
        author = request.user
        description = form.cleaned_data['description']
        Vacancy.objects.create(author=author, description=description)
    return redirect('/home')
    



