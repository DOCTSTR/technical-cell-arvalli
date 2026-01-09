from django.db import models


class Case(models.Model):
    fir_number = models.CharField(max_length=100)
    police_station = models.CharField(max_length=200)
    incident_date = models.DateField()
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fir_number


class CasePerson(models.Model):
    STATUS_CHOICES = (
        ("ACCUSED", "Accused"),
        ("WANTED", "Wanted"),
        ("ARRESTED", "Arrested"),
    )

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name="persons"
    )

    full_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    photo = models.ImageField(
        upload_to="case_person/photos/",
        null=True,
        blank=True
    )

    # ✅ NEW – FILE / PDF ATTACHMENT
    documents = models.FileField(
        upload_to="case_person/documents/",
        null=True,
        blank=True,
        help_text="Upload PDF / image / document"
    )

    address = models.TextField(blank=True)
    taluka = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

    mobile_numbers = models.TextField(
        blank=True,
        help_text="Comma separated mobile numbers"
    )

    urls = models.TextField(blank=True)
    bank_details = models.TextField(blank=True)
    family_details = models.TextField(blank=True)
    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
