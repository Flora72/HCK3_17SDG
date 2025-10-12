from django import forms

class AgroForm(forms.Form):
    SOIL_CHOICES = [
        ('sandy', 'Sandy'),
        ('clay', 'Clay'),
        ('loamy', 'Loamy'),
        ('rocky', 'Rocky'),
    ]
    RAINFALL_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]

    soil = forms.ChoiceField(choices=SOIL_CHOICES, label="Soil Type")
    rainfall = forms.ChoiceField(choices=RAINFALL_CHOICES, label="Rainfall Level")
    land_size = forms.FloatField(label="Land Size (in acres)", min_value=0.1)
    phone_number = forms.CharField(label="Phone Number", max_length=15)
