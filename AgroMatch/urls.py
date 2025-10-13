from django.urls import path
from .views import agro_form_view, home_view, login_view, signup_view, logout_view


urlpatterns = [
    path('', home_view, name='home'),
    path('recommend/', agro_form_view, name='agro_form'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),

]
