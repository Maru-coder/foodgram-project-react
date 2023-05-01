import os
from sys import stdout

from cleo.formatters import style

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodgram.settings')
import django
django.setup()

import csv
from django.conf import settings
from django.core.management import BaseCommand

from recipes.models import Ingredient

def handle(*args, **kwargs):
    with open(
            'E:\\foodgram-project-react\\data\\ingredients.csv',
            'r',
            encoding='utf-8'
    ) as file:
        fieldnames = ['name', 'measurement_unit']
        csv_reader = csv.DictReader(file, fieldnames=fieldnames)
        for row in csv_reader:
            my_model = Ingredient.objects.create(
                name=row['name'],
                measurement_unit=row['measurement_unit']
            )

handle()


