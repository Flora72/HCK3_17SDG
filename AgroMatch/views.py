
from django.shortcuts import render, redirect # Import redirect for signup
from django.contrib.auth.decorators import login_required # IMPORT THIS
from django.contrib.auth.forms import UserCreationForm # IMPORT THIS for signup
from .forms import AgroForm
from .utils import recommend_crop
from .messaging import generate_message

def signup_view(request):
    """Handles user registration using Django's built-in form."""
    if request.method == 'POST':
        # Use the built-in form for simplicity
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect('login') 
    else:
        form = UserCreationForm()
        
    # Pass the form to the signup.html template
    return render(request, 'signup.html', {'form': form})

@login_required
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
