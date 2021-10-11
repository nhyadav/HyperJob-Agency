from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.MyLoginView.as_view()),
    path('signup', views.MySignupView.as_view()),
    path('home', views.homepage, name='home page'),
    path("vacancies/", include("vacancy.urls")),
    path('vacancy/', include('vacancy.urls')),
    path('resumes/', include("resume.urls")),
    path('resume/', include('resume.urls'))
    
]
