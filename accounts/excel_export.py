from openpyxl import Workbook
from django.http import HttpResponse


def export_cases_to_excel(modeladmin, request, queryset):
    wb = Workbook()
    ws = wb.active
    ws.title = "Cases"

    ws.append([
        "FIR Number",
        "Police Station",
        "Crime Date",
        "Full Name",
        "Age",
        "Status",
        "Address",
        "Taluka",
        "District",
        "State",
        "Mobile Number",
        "Bank Details",
        "URLs",
        "Family Details",
        "Remarks",
    ])

    for case in queryset:
        for person in case.persons.all():
            ws.append([
                case.fir_number,
                case.police_station,
                case.crime_date,
                person.full_name,
                person.age,
                person.status,
                person.address,
                person.taluka,
                person.district,
                person.state,
                person.mobile_number,
                person.bank_details,
                person.urls,
                person.family_details,
                person.remarks,
            ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=cases.xlsx"
    wb.save(response)
    return response


def export_nasta_farta_to_excel(modeladmin, request, queryset):
    wb = Workbook()
    ws = wb.active
    ws.title = "Nasta Farta"

    ws.append([
        "Reference Number",
        "Police Station",
        "Incident Date",
        "Full Name",
        "Age",
        "Status",
        "Address",
        "Taluka",
        "District",
        "State",
        "Mobile Number",
        "Bank Details",
        "URLs",
        "Family Details",
        "Remarks",
    ])

    for nf in queryset:
        for person in nf.persons.all():
            ws.append([
                nf.reference_number,
                nf.police_station,
                nf.incident_date,
                person.full_name,
                person.age,
                person.status,
                person.address,
                person.taluka,
                person.district,
                person.state,
                person.mobile_number,
                person.bank_details,
                person.urls,
                person.family_details,
                person.remarks,
            ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=nasta_farta.xlsx"
    wb.save(response)
    return response
