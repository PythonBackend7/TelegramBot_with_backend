from django.contrib import admin
from .models import Todo
# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title', 'created_at')
    search_fields = ('title', )