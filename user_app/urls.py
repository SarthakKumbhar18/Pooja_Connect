from django.urls import path,include
from .views import *

urlpatterns = [
    path('user_signup/',user_signup_view,name="user_signup"),
    path('user_signin/',user_signin_view,name="user_signin"),
    path('user_homepage/<int:id>/',user_homepage_view,name="user_homepage"),
    path('user_appointment/',appointment_booking,name="user_appointment"),
    path('user_signout/',user_signout_view,name="user_signout"),
    path('user_appointment_table/<int:id>/',user_appointment_table_view,name="user_appointment_table"),    
    path('update_appointment/<int:id>/',update_appointment_view,name="update_appointment"),    
    path('delete_appointment/<int:id>/',delete_appointment_view,name="delete_appointment"),    
    
]