from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import NastaFarta
from cases.models import Case, CasePerson


# =====================================================
# DASHBOARD
# =====================================================
def dashboard(request):
    q = request.GET.get("q", "").strip()

    # =================================================
    # NASTA FARTA SEARCH
    # =================================================
    nasta_qs = NastaFarta.objects.all().order_by("-id")

    if q:
        nasta_qs = nasta_qs.filter(
            Q(full_name__icontains=q) |
            Q(taluka__icontains=q) |
            Q(district__icontains=q) |
            Q(status__icontains=q) |
            Q(address__icontains=q) |
            Q(phone_numbers__icontains=q)
        )

    latest_nasta = nasta_qs[:3]
    all_nasta = nasta_qs

    # =================================================
    # NASTA COUNTS (DONUT)
    # =================================================
    arvalli_count = nasta_qs.filter(status="ARVALLI").count()
    gujarat_other_count = nasta_qs.filter(status="GUJARATSTATE").count()
    outside_count = nasta_qs.filter(status="OUTSIDEGUJARAT").count()
    total_nasta = nasta_qs.count()

    # =================================================
    # FIR / CASE SEARCH (THIS IS THE FIX)
    # =================================================
    case_qs = Case.objects.all().order_by("-id")

    if q:
        case_qs = case_qs.filter(
            Q(fir_number__icontains=q) |
            Q(police_station__icontains=q) |
            Q(remarks__icontains=q) |
            Q(persons__full_name__icontains=q) |
            Q(persons__mobile_numbers__icontains=q) |
            Q(persons__address__icontains=q)
        ).distinct()

    cases = case_qs

    # =================================================
    # FIR COUNTS (FROM CasePerson)
    # =================================================
    total_fir = case_qs.count()

    arrested_count = CasePerson.objects.filter(status="ARRESTED").count()
    wanted_count = CasePerson.objects.filter(status="WANTED").count()
    accused_count = CasePerson.objects.filter(status="ACCUSED").count()

    # =================================================
    # CONTEXT
    # =================================================
    context = {
        # Nasta
        "latest_nasta": latest_nasta,
        "all_nasta": all_nasta,
        "arvalli_count": arvalli_count,
        "gujarat_other_count": gujarat_other_count,
        "outside_count": outside_count,
        "total_nasta": total_nasta,

        # FIR
        "cases": cases,
        "total_fir": total_fir,
        "arrested_count": arrested_count,
        "wanted_count": wanted_count,
        "accused_count": accused_count,
    }

    return render(request, "accounts/dashboard.html", context)


# =====================================================
# NASTA DETAIL
# =====================================================
def dashboard_nasta_detail(request, nasta_id):
    nasta = get_object_or_404(NastaFarta, id=nasta_id)
    return render(
        request,
        "accounts/dashboard_nasta_detail.html",
        {"nasta": nasta},
    )


# =====================================================
# CASE DETAIL
# =====================================================
def dashboard_case_detail(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    persons = CasePerson.objects.filter(case=case)

    return render(
        request,
        "accounts/dashboard_case_detail.html",
        {
            "case": case,
            "persons": persons,
        },
    )


# =====================================================
# SAFE PLACEHOLDERS (DO NOT BREAK URLS)
# =====================================================
def dashboard_case_pdf(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    return render(request, "accounts/pdf_placeholder.html", {"case": case})


def export_fir_persons_excel(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    persons = CasePerson.objects.filter(case=case)
    return render(
        request,
        "accounts/export_placeholder.html",
        {"case": case, "persons": persons},
    )
from django.shortcuts import render, get_object_or_404
from .models import NastaFarta

def dashboard_nasta_detail(request, nasta_id):
    nasta = get_object_or_404(NastaFarta, id=nasta_id)
    return render(
        request,
        'accounts/dashboard_nasta_detail.html',
        {'nasta': nasta}
    )
