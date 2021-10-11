from django.shortcuts import render, redirect
from django.http import request, HttpResponseForbidden
from .models import Resume
from .form import Resumeform
from django.core.exceptions import PermissionDenied
# Create your views here.
def resume(request):
    resume = Resume.objects.all()
    return render(request, "resume/resume.html", {'resume': resume})

def create_resume(request):
    if request.method=='POST':
        can_create = request.user.is_authenticated and not request.user.is_staff
        if not can_create:
            # raise PermissionDenied
            return HttpResponseForbidden(status=403)

        form = Resumeform(request.POST)
        if not form.is_valid():
            return HttpResponseForbidden(status=403)
        author = request.user
        description = form.cleaned_data['description']
        Resume.objects.create(author=author, description=description)
    return redirect('/home')

