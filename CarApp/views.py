from django.shortcuts import render
from .models import Car,Brand


def HomeView(request):
    car1 = Car.objects.all().order_by('id')[0]
    brands = Brand.objects.all()
    electric_cars = Car.objects.filter(engine='ELEKTR').order_by('id')[:5]
    cars_by_brand = Car.objects.all()
    
    
    context = {
        'car1': car1,
        'brands': brands,
        'electric_cars': electric_cars,
        'cars_by_brand':  cars_by_brand
        
    }
    
    return render(request, 'index.html',context)


