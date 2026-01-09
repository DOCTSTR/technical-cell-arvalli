from django.contrib import admin
from .models import Case, CasePerson


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "fir_number",
        "police_station",
        "incident_date",
        "created_at",
    )

    search_fields = ("fir_number", "police_station")
    list_filter = ("police_station",)
    readonly_fields = ("created_at",)


@admin.register(CasePerson)
class CasePersonAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "status",
        "case",
    )

    search_fields = ("full_name",)
    list_filter = ("status",)
