from django.shortcuts import render,HttpResponse

# Create your views here.
def astro_home_view(request):
    return render(request,"Astro_app/astro_home.html")

def horoscope_view(request):
    return render(request,"Astro_app/horoscope.html")

def numerology_view(request):
    return render(request,"Astro_app/numerology.html")

def kundli_view(request):
    return render(request,"Astro_app/kundli.html")

def panchang_view(request):
    return render(request,"Astro_app/panchang.html")

def grahadasha_view(request):
    return render(request,"Astro_app/grahadasha.html")

def gemstone_view(request):
    return render(request,"Astro_app/gemstone.html")



