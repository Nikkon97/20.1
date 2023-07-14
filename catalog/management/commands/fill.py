from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'title': 'test_1', 'price': 1},
            {'title': 'test_2', 'price': 2},
            {'title': 'test_3', 'price': 3},
            {'title': 'test_4', 'price': 4},
            {'title': 'test_5', 'price': 5},
            {'title': 'test_6', 'price': 6}
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
