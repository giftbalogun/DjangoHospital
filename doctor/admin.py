from django.contrib import admin

# Register your models here.

from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Doctor, DoctorAdmin)
