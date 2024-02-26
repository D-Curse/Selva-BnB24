import random
from django.core.management.base import BaseCommand
from faker import Faker
from coreApp.models import Animal, IndividualAnimal

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def add_arguments(self, parser):
        parser.add_argument('--animal_types', type=int, default=5, help='Number of animal types to create')
        parser.add_argument('--individual_animals_per_type', type=int, default=10, help='Number of individual animals per type to create')

    def handle(self, *args, **options):
        fake = Faker()
        Animal.objects.all().delete()
        IndividualAnimal.objects.all().delete()

        # Create fake animal types
        for _ in range(options['animal_types']):
            animal_type = Animal.objects.create(
                animal_type=fake.word(['lion','tiger','elephant']),
                sex_ratio=fake.word(),
                population=random.randint(50, 500)
            )

            # Create fake individual animals for each type
            for _ in range(options['individual_animals_per_type']):
                IndividualAnimal.objects.create(
                    animal_type=fake.word(),
                    nickname=fake.first_name(),
                    age=random.randint(15, 60),
                    sex=random.choice(['Male', 'Female']),
                    health=random.choice(['Healthy','Weak'])
                )

        self.stdout.write(self.style.SUCCESS('Fake data successfully populated.'))

