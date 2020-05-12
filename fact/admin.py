from django.contrib import admin

# Register your models here.

from .models import Fact


class FactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Fact, FactAdmin)
