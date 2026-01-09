from django.core.management.base import BaseCommand

from accounts.models import CasePerson as NewCasePerson, FIRCase
from cases.models import CasePerson as OldCasePerson


class Command(BaseCommand):
    help = "Sync extra fields from cases.CasePerson to accounts.CasePerson"

    def handle(self, *args, **options):
        updated = 0
        skipped = 0

        for old in OldCasePerson.objects.select_related("case"):
            try:
                fir = FIRCase.objects.get(fir_number=old.case.fir_number)
            except FIRCase.DoesNotExist:
                skipped += 1
                continue

            try:
                new = NewCasePerson.objects.get(
                    case=fir,
                    full_name=old.full_name
                )
            except NewCasePerson.DoesNotExist:
                skipped += 1
                continue

            changed = False

            fields = [
                "mobile_numbers",
                "address",
                "bank_details",
                "family_details",
                "urls",
                "photo",
            ]

            for field in fields:
                old_value = getattr(old, field, None)
                new_value = getattr(new, field, None)

                if old_value and not new_value:
                    setattr(new, field, old_value)
                    changed = True

            if changed:
                new.save()
                updated += 1
            else:
                skipped += 1

        self.stdout.write(self.style.SUCCESS("CasePerson extra field sync complete"))
        self.stdout.write(self.style.SUCCESS(f"Updated: {updated}"))
        self.stdout.write(self.style.WARNING(f"Skipped: {skipped}"))
