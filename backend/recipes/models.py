from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from recipes.utils.consts import (
    MIN_INGREDIENT_AMOUNT,
    MAX_INGREDIENT_AMOUNT,
    MIN_COOCKING_TIME,
    MAX_COOCKING_TIME
)

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField('Название ингредиента', max_length=200)
    measurement_unit = models.CharField(
        'Единица измерения ингредиента', max_length=200
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    name = models.CharField('Имя', max_length=60, unique=True)
    color = models.CharField('Цвет', max_length=7, unique=True)
    slug = models.SlugField('Ссылка', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField('Название рецепта', max_length=255)
    image = models.ImageField(
        'Изображение рецепта',
        upload_to='static/recipe/',
        blank=True,
        null=True,
    )
    text = models.TextField('Описание рецепта')
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления рецепта',
        validators=[
            MinValueValidator(
                MIN_COOCKING_TIME,
                message='Время приготовления должно быть больше 0!'
            ),
            MaxValueValidator(
                MAX_COOCKING_TIME,
                message='Время приготовления не должно превышать 24 часов.'
            )
        ],
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient'),
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        Tag, verbose_name='Тэги', related_name='recipes'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredient_list'
    )
    ingredient = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE, related_name='ingredient'
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
        validators=[
            MinValueValidator(
                MIN_INGREDIENT_AMOUNT,
                message='Количество ингредиента должно быть больше 0!'
            ),
            MaxValueValidator(
                MAX_INGREDIENT_AMOUNT,
                message='Количество ингредиента не должно превышать 32000.'
            )
        ],
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецепте'

    def __str__(self):
        return (
            f'{self.ingredient.name} ({self.ingredient.measurement_unit})'
            f' - {self.amount}'
        )


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='favorite_recipe',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite_recipe',
        verbose_name='Избранный рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        null=True,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Покупка',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Список покупок'
