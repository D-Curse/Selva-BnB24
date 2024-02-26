from django.contrib import admin
from .models import Animal, IndividualAnimal, Habitat

# Register your models here.

admin.site.register(Animal)
admin.site.register(IndividualAnimal)
admin.site.register(Habitat)