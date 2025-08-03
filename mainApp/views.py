from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    return redirect('login')