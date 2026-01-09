from django.contrib import admin
from .models import NastaFarta


@admin.register(NastaFarta)
class NastaFartaAdmin(admin.ModelAdmin):
    """
    Safe Admin configuration for Nasta Farta
    """

    # =========================
    # LIST VIEW
    # =========================
    list_display = (
        "id",
        "full_name",
        "status",
        "taluka",
        "district",
        "created_at",
    )

    list_filter = (
        "status",
        "district",
    )

    search_fields = (
        "full_name",
        "taluka",
        "district",
        "phone_numbers",
    )

    ordering = ("-id",)

    # =========================
    # FORM LAYOUT
    # =========================
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "full_name",
                    "status",
                    "taluka",
                    "district",
                )
            },
        ),
        (
            "Personal Details",
            {
                "fields": (
                    "photo",
                    "address",
                    "phone_numbers",
                )
            },
        ),
        (
            "Financial & Family Details",
            {
                "fields": (
                    "bank_details",
                    "family_details",
                )
            },
        ),
        (
            "Links & References",
            {
                "fields": (
                    "urls",
                    "other_cases",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
