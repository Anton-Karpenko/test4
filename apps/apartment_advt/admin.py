from django.contrib import admin

from .models import ApartmentAdvt


@admin.register(ApartmentAdvt)
class ApartmentAdvtAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
