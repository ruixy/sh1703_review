from django.contrib import admin

# Register your models here.
from . import models

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'finish', 'title')

admin.site.register(models.Todo, TodoAdmin)