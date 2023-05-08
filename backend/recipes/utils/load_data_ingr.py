import csv
import os

import django

from recipes.models import Ingredient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodgram.settings')

django.setup()


def handle(*args, **kwargs):
    with open(
        'E:\\foodgram-project-react\\data\\ingredients.csv',
        'r',
        encoding='utf-8',
    ) as file:
        fieldnames = ['name', 'measurement_unit']
        csv_reader = csv.DictReader(file, fieldnames=fieldnames)
        for row in csv_reader:
            Ingredient.objects.create(
                name=row['name'], measurement_unit=row['measurement_unit']
            )


handle()
