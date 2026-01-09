from django.db import models
from django.utils import timezone


class NastaFarta(models.Model):
    """
    Nasta Farta Master Record
    """

    STATUS_CHOICES = [
        ("ARVALLI", "Arvalli District"),
        ("GUJARATSTATE", "Other District (Gujarat State)"),
        ("OUTSIDEGUJARAT", "Outside Gujarat"),
    ]

    # =========================
    # BASIC INFORMATION
    # =========================
    full_name = models.CharField(
        max_length=255
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    taluka = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # =========================
    # PERSONAL DETAILS
    # =========================
    photo = models.ImageField(
        upload_to="nasta_farta/photos/",
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    phone_numbers = models.TextField(
        help_text="Comma separated phone numbers",
        blank=True,
        null=True
    )

    # =========================
    # FINANCIAL & FAMILY DETAILS
    # =========================
    bank_details = models.TextField(
        blank=True,
        null=True
    )

    family_details = models.TextField(
        blank=True,
        null=True
    )

    # =========================
    # LINKS & REFERENCES
    # =========================
    urls = models.TextField(
        help_text="Any related URLs / links",
        blank=True,
        null=True
    )

    other_cases = models.TextField(
        help_text="Reference to other FIRs / cases (text only)",
        blank=True,
        null=True
    )

    # =========================
    # SYSTEM FIELDS
    # =========================
    created_at = models.DateTimeField(
        default=timezone.now
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =========================
    # META
    # =========================
    class Meta:
        verbose_name = "Nasta Farta"
        verbose_name_plural = "Nasta Fartas"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.full_name} ({self.status})"
