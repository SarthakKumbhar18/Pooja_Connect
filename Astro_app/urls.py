from django.urls import path,include
from .views import *
urlpatterns = [
    path('astro/',astro_home_view,name="astro_home"),
    path('horoscope/',horoscope_view,name="horoscope"),
    path('numerology/',numerology_view,name="numerology"),
    path('kundli/',kundli_view,name="kundli"),
    path('panchang/',panchang_view,name="panchang"),
    path('grahadasha/',grahadasha_view,name="grahadasha"),
    path('gemstone/',gemstone_view,name="gemstone"),
]