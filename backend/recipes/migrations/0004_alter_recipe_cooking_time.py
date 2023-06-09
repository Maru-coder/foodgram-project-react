# Generated by Django 3.2 on 2023-05-04 07:15

import django.core.validators

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0003_auto_20230503_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, message='Время приготовления должно быть больше 0!'
                    )
                ],
                verbose_name='Время приготовления рецепта',
            ),
        ),
    ]
