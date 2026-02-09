from django.contrib import admin
from .models import patients
# Register your models here.

@admin.register(patients)
class PatientAdmin(admin.ModelAdmin):
    list_display=("id","name","age","disease_type")
    search_fields=("name",)
    list_filter=("disease_type",)
    list_display_links=("name",)

