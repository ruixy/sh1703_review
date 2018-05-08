# -*- encoding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from . import models
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'todo_id',

    )

admin.site.register(models.Todo)
admin.site.register(models.Employee, EmployeeAdmin)