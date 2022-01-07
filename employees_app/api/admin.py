from django.contrib import admin

from .models import Department, ProgrammingLanguage, Employee


@admin.register(Department)
class MeterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'floor']
    search_fields = ['name', ]
    fields = ['name', 'floor']
    readonly_fields = ['id']


@admin.register(ProgrammingLanguage)
class MeterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', ]
    fields = ['name', ]
    readonly_fields = ['id']


@admin.register(Employee)
class MeterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'age', 'department', 'programming_language']
    search_fields = ['name', 'last_name']
    fields = ['name', 'last_name', 'age', 'department', 'programming_language']
    readonly_fields = ['id']


# Register your models here.
