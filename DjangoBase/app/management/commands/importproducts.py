import json
from django.core.management.base import BaseCommand
from app.models import Product

class Command(BaseCommand):
    """Import products from a JSON file.
    """
    help = 'Import products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        filename = options['filename']
        with open(filename, 'r') as f:
            data = json.load(f)
            for product_data in data:
                product = Product(**product_data)
                product.save()
        self.stdout.write(self.style.SUCCESS('Products imported successfully.'))
