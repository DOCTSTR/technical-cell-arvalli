from django.core.management.base import BaseCommand

from accounts.models import FIRCase, CasePerson as NewCasePerson
from cases.models import Case as OldCase
from cases.models import CasePerson as OldCasePerson


class Command(BaseCommand):
    help = "One-time migration: copy cases.CasePerson into accounts.CasePerson"

    def handle(self, *args, **options):
        created = 0
        skipped = 0

        for old_person in OldCasePerson.objects.select_related("case"):
            try:
                # Match FIRCase using FIR number
                fir = FIRCase.objects.get(
                    fir_number=old_person.case.fir_number
                )
            except FIRCase.DoesNotExist:
                skipped += 1
                continue

            # Avoid duplicates (same person + same FIR)
            if NewCasePerson.objects.filter(
                case=fir,
                full_name=old_person.full_name,
                status=old_person.status
            ).exists():
                skipped += 1
                continue

            NewCasePerson.objects.create(
                case=fir,
                full_name=old_person.full_name,
                status=old_person.status
            )
            created += 1

        self.stdout.write(self.style.SUCCESS("CasePerson migration complete"))
        self.stdout.write(self.style.SUCCESS(f"Created: {created}"))
        self.stdout.write(self.style.WARNING(f"Skipped: {skipped}"))
