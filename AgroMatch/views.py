from django.shortcuts import render
from .forms import AgroForm
from .utils import recommend_crop
from .messaging import generate_message

def home_view(request):
    return render(request, 'index.html')

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
