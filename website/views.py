from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    """check to see if user logged in"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psswrd']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged In.")
            return redirect('home')
        if user is None:
            messages.success(request, "Incorrect Username or password, try again.")
            return redirect('home')
        
    return render(request, 'home.html', {})


def logout_user(request):
    """Check to see if user logged out"""
    logout(request)
    messages.success(request, "You've been logged out...")
    return redirect('home')
