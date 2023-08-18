from django.core.management import BaseCommand

from database.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'продукты', 'decrp': 'продукты питания'},
            {'name': 'Электроника', 'decrp': 'цифровая техника'},
            {'name': 'мебель', 'decrp': 'мебель своими руками'},
            {'name': 'мягкая мебель', 'decrp': 'кресла'},

            ]

        category_for_create = []

        for category_item in category_list:
            category_for_create.append(Category(**category_item))


        Category.objects.bulk_create(category_for_create)