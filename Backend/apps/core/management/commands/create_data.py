import requests 

from django.utils.text import slugify

from django.core.management import BaseCommand

from apps.categories.models import Category
from apps.products.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get('https://dummyjson.com/products')
        if response.status_code == 200:
            products = response.json().get('products', [])

        for product in products:
            category, _ = Category.objects.get_or_create(
                title = product['category'],
                slug= slugify(product['category']),
            )
            Product.objects.create(
                category = category,
                title = product['title'],
                slug=slugify(product['title']),
                price = product['price'],
                thumbnail = product['thumbnail'],
                description = product['description']
            )