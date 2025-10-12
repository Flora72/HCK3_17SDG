from django.urls import path
from .views import agro_form_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('recommend/', agro_form_view, name='agro_form'),


]
