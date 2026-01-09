from django import forms
from .models import Case


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            "FIR_NUMBER",
            "CASE_TITLE",
            "SECTIONS",
            "POLICE_STATION",
            "DISTRICT",
            "DESCRIPTION",
        ]
from .models import Accused


class AccusedForm(forms.ModelForm):
    class Meta:
        model = Accused
        fields = [
            "NAME",
            "ALIAS",
            "CATEGORY",
            "PHOTO",
            "CASE",
            "WANTED_SINCE",
            "LAST_SEEN_LOCATION",
            "BANK_DETAILS",
            "FAMILY_DETAILS",
            "PHONE_NUMBER",
            "EMAIL",
            "REMARKS",
        ]
