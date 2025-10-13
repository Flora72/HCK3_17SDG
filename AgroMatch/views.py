
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import AgroForm
from .utils import recommend_crop
from .messaging import generate_message
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('agro_form')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
def home_view(request):
    return render(request, 'index.html')

@login_required
def agro_form_view(request):
    if request.method == 'POST':
        form = AgroForm(request.POST)
        if form.is_valid():
            soil = form.cleaned_data['soil']
            rainfall = form.cleaned_data['rainfall']
            land_size = form.cleaned_data['land_size']

            # Rule-based recommendation
            crop, practice = recommend_crop(soil, rainfall, land_size)
            message = generate_message(crop, practice)

            return render(request, 'results.html', {
                'crop': crop,
                'practice': practice,
                'message': message
            })
    else:
        form = AgroForm()
    return render(request, 'form.html', {'form': form})
