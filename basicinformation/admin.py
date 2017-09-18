from django.contrib import admin

# Register your models here.
from .models import (
    Information
)


class InformationDisplay(admin.ModelAdmin):
    readonly_fields = ('creation_date', )
    fieldsets = [
        ('Account Created', {'fields': ['creation_date']}),
        ('Primary Email', {'fields': ['email']}),
        ('User Information', {'fields': ['first_name', 'middle_name', 'last_name', 'age', 'location']})
    ]

    list_display = ['first_name', 'middle_name', 'last_name', 'creation_date']

    list_filter = ['creation_date']

admin.site.register(Information, InformationDisplay)
# @admin.register(Information)
# class InformationAdmin(admin.ModelAdmin):
#     list_display = [
#         'first_name','last_name','location','age','email','creation_date'
#     ]
