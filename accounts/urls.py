from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # FIR Case Detail (already working)
    path('case/<int:case_id>/', views.dashboard_case_detail, name='dashboard_case_detail'),

    # ✅ NASTA FARTA DETAIL (MISSING — NOW FIXED)
    path('nasta/<int:nasta_id>/', views.dashboard_nasta_detail, name='dashboard_nasta_detail'),
]
