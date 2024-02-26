from django.db import models

# Create your models here.

class Habitat(models.Model):
    habitat_type = models.CharField(max_length=50, unique=True)
    habitat_description = models.TextField(null=True, blank=True)
    habitat_image = models.ImageField(upload_to='img/habitat_img/', blank=True, null=True)

    def __str__(self):
        return self.habitat_type

class Animal(models.Model):
    animal_type = models.CharField(max_length=100, unique=True)
    population = models.IntegerField()
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.animal_type
    
class IndividualAnimal(models.Model):
    animal_type = models.ForeignKey(Animal, on_delete=models.CASCADE)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE, related_name='animals', blank=True, null=True)
    nickname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    health = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nickname} ({self.animal_type.animal_type})" 