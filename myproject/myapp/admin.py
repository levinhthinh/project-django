from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Book)
class Bookadmin(admin.ModelAdmin):
    list_display=('Title','Author','Description','Price','Created_at')
    search_fields=('Title','Author')

@admin.register(models.Keyboard)
class Bookadmin(admin.ModelAdmin):
    list_display=('Name','Image','Price','Short_Description','Material','Place_of_Origin','Length','Width','Height')
    search_field=('Name')

    