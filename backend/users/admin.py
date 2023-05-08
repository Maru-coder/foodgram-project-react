from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import Subscribe

User = get_user_model()


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'date_joined',
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('date_joined', 'email', 'first_name')


@admin.register(Subscribe)
class SubscribeAdmin(BaseAdmin):
    list_display = (
        'user',
        'author',
    )
