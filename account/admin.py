from django.contrib import admin

from . import models


@admin.register(models.MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nickname')
    list_per_page = 20

