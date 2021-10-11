from django.urls import path
from . import views


urlpatterns = [
    path('', views.vacancy, name='home'),
    path('new', views.new_vacancy, name='new vacancy')
   
]
