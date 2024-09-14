from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to home or next page
            return redirect('home')
        # If the form is not valid, the same page with form errors is rendered
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = ProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            # Save the changes to the user object
            form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'blog/profile.html', context)
