# yourapp/management/commands/delete_all_data.py
from django.core.management.base import BaseCommand
from coreApp.models import Animal, IndividualAnimal

class Command(BaseCommand):
    help = 'Delete all data from Animal and IndividualAnimal models'

    def handle(self, *args, **options):
        Animal.objects.all().delete()
        IndividualAnimal.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('All data successfully deleted.'))
