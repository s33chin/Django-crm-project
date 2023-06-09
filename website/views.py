from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm



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

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
            
    return render(request, 'register.html', {})
    
