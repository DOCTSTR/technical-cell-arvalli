from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import NastaFarta
from cases.models import Case, CasePerson


# ======================================================
# SIMPLE HTML → PDF RESPONSE (NO EXTERNAL LIB)
# ======================================================
def html_to_pdf_response(html, filename):
    response = HttpResponse(html, content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="{filename}"'
    return response


# ======================================================
# PERSON (NASTA FARTA) PDF
# URL NAME: person_pdf
# ======================================================
@login_required
def person_pdf(request, pk):
    person = get_object_or_404(NastaFarta, pk=pk)

    html = render_to_string(
        "accounts/pdf/person_pdf.html",
        {"person": person}
    )

    return html_to_pdf_response(html, f"nasta_farta_{person.id}.pdf")


# ======================================================
# FIR CASE PDF
# URL NAME: dashboard_case_pdf
# ======================================================
@login_required
def fir_case_pdf(request, pk):
    case = get_object_or_404(Case, pk=pk)
    persons = CasePerson.objects.filter(case=case)

    html = render_to_string(
        "accounts/pdf/fir_case_pdf.html",
        {
            "case": case,
            "persons": persons,
        }
    )

    return html_to_pdf_response(html, f"fir_case_{case.id}.pdf")
