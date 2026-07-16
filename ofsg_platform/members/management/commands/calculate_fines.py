from django.core.management.base import BaseCommand
from django.utils import timezone
from members.models import Member, Contribution, Fine
from decimal import Decimal


class Command(BaseCommand):
    help = 'Automatically checks for late contributions and applies fines'

    def handle(self, *args, **kwargs):
        today = timezone.now()
        # Rule: Only check if past the 10th of the month
        if today.day > 10:
            members = Member.objects.all()
            for member in members:
                # Check if they have paid this month
                has_paid = Contribution.objects.filter(
                    member=member,
                    date_paid__month=today.month,
                    date_paid__year=today.year
                ).exists()

                if not has_paid:
                    # Apply 20% fine as per the constitution
                    fine_amount = Decimal('200.00')  # Example: 20% of 1000 contribution
                    Fine.objects.get_or_create(
                        member=member,
                        fine_type="Late Payment",
                        amount=fine_amount,
                        is_paid=False
                    )
                    self.stdout.write(f"Fine applied to {member.username}")
