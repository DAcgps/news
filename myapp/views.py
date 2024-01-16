from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html',{'articles': articles})

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'
