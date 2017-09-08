from django.contrib import admin

# Register your models here.
from .models import (
    Information
)

#admin.site.register(Information)
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = [
        'first_name','last_name','location','age','email','creation_date'
    ]