from django.core.management.base import BaseCommand
from datetime import date
from your_app.models import Category, Product

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        self.stdout.write("Clearing old data from the database...")
        Category.objects.all().delete()
        Product.objects.all().delete()

        self.stdout.write("Populating database with new data...")
        # Создание новых объектов и сохранение их в базе данных
        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')

        Product.objects.create(name='Product 1', category=category1, unit_price=10)
        Product.objects.create(name='Product 2', category=category2, unit_price=20)

        self.stdout.write(self.style.SUCCESS("Database has been populated successfully"))