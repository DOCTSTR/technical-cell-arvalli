import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import NastaFarta
from cases.models import Case, CasePerson


# ======================================================
# EXPORT NASTA FARTA (ALL RECORDS)
# ======================================================
@login_required
def export_nasta_farta(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="nasta_farta.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "ID",
        "Full Name",
        "Status",
        "Mobile Numbers",
        "Taluka",
        "District",
        "Address",
        "Bank Details",
        "Family Details",
        "URLs",
        "Created At",
    ])

    for obj in NastaFarta.objects.all().order_by("-created_at"):
        writer.writerow([
            obj.id,
            obj.full_name,
            obj.status,
            obj.mobile_numbers,
            obj.taluka,
            obj.district,
            obj.address,
            obj.bank_details,
            obj.family_details,
            obj.urls,
            obj.created_at,
        ])

    return response


# ======================================================
# EXPORT FIR CASES (CASE REGISTER)
# ======================================================
@login_required
def export_fir_cases(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="fir_cases.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "Case ID",
        "FIR Number",
        "Police Station",
        "Incident Date",
        "Created At",
    ])

    for case in Case.objects.all().order_by("-created_at"):
        writer.writerow([
            case.id,
            case.fir_number,
            case.police_station,
            case.incident_date,
            case.created_at,
        ])

    return response


# ======================================================
# EXPORT PERSONS OF A SPECIFIC FIR
# ======================================================
@login_required
def export_fir_persons_excel(request, case_id):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        f'attachment; filename="fir_case_{case_id}_persons.csv"'
    )

    writer = csv.writer(response)
    writer.writerow([
        "Case ID",
        "Full Name",
        "Status",
        "Mobile Numbers",
        "Address",
        "Bank Details",
        "Family Details",
        "URLs",
    ])

    persons = CasePerson.objects.filter(case_id=case_id)

    for p in persons:
        writer.writerow([
            p.case_id,
            p.full_name,
            p.status,
            p.mobile_numbers,
            p.address,
            p.bank_details,
            p.family_details,
            p.urls,
        ])

    return response
