from django.urls import path
from . import views


urlpatterns = [
    path('', views.resume, name='home'),
    path('new', views.create_resume, name='new resume')


]
