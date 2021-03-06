from django.contrib import admin
from .models import Blog, Category, Comment

# Register your models here.

admin.site.site_header = 'PrimaVie Pharmacy Care'

admin.site.register(Blog)
admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
