from django.urls import path,include
from .views import *

urlpatterns = [
    path('pandit_profile/<int:id>/',pandit_profile_view,name="pandit_profile"),
    path('pandit_signup/',pandit_signup_view,name="pandit_signup"),
    path('pandit_signin/',pandit_signin_view,name="pandit_signin"),
    path('pandit_signout/',pandit_signout_view,name="pandit_signout"),
    path('appointment_confirmation/<int:id>',appointment_confirmation_view,name="appointment_confirmation"),
    path('appointment_declined/<int:id>',appointment_declined_view,name="appointment_declined"),
    path('',main_home_view,name="main_home")

    
]