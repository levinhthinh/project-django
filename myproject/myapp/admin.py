from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Book)
class Bookadmin(admin.ModelAdmin):
    list_display=('Title','Author','Description','Price','Created_at')
    search_fields=('Title','Author')

    