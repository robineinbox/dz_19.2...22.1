from django.core.management.base import BaseCommand
from main.models import Category, Product


class Command(BaseCommand):
    help = 'Populate the database with data'

    def handle(self, *args, **options):
        self.populate_categories()
        self.populate_products()

    def populate_categories(self):
        Category.objects.all().delete()

        categories = [
            {'name': 'Category 1', 'description': 'Description 1'},
            {'name': 'Category 2', 'description': 'Description 2'},
            {'name': 'Category 3', 'description': 'Description 3'},
        ]

        for category_data in categories:
            Category.objects.create(
                name=category_data['name'],
                description=category_data['description']
            )

    def populate_products(self):
        Product.objects.all().delete()

        products = [
            {'name': 'Product 1', 'description': 'Description 1', 'category_name': 'Category 1', 'unit_price': 10},
            {'name': 'Product 2', 'description': 'Description 2', 'category_name': 'Category 2', 'unit_price': 20},
        ]

        for product_data in products:
            category = Category.objects.get(name=product_data['category_name'])

            Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                category=category,
                unit_price=product_data['unit_price']
            )