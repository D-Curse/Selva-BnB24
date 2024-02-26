from django.shortcuts import render, get_object_or_404
from .models import Habitat, IndividualAnimal       

# Create your views here.

def home(request):
    return render(request, 'core/habitat_selection.html')

def selection(reqest):
    return render(reqest, 'core/habitat_selection.html')


def habitat_section(request, habitat_type):
    selected_habitat = get_object_or_404(Habitat, habitat_type=habitat_type)
    related_animals = selected_habitat.animals.all()

    unique_animal_types = set(animal.animal_type for animal in related_animals)

    context = {
        'selected_habitat': selected_habitat,
        'related_animals': related_animals,
        'unique_animal_types': unique_animal_types,
    }
    
    print(context)
    for animals in related_animals:
        print(animals.id)

    return render(request, 'core/habitat_details.html', context)

def data_enter(request):
    
    individual_animals = IndividualAnimal.objects.all()
    
    return render(request, 'core/data_enter.html', {'individual_animals':individual_animals})