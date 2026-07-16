from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Custom Member Model (linked to the Constitution's membership rules)
class Member(AbstractUser):
    # Inherits from Django's User model (handles auth/security)
    phone_number = models.CharField(max_length=15)
    is_active_member = models.BooleanField(default=True)
    registration_date = models.DateField(auto_now_add=True)

    # Constitution constraint: Max 115 members
    class Meta:
        verbose_name = "Member"

# 2. Financials (Savings and Welfare)
class Contribution(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contribution_type = models.CharField(max_length=50)  # e.g., 'Monthly', 'Welfare', 'AGM'
    date_paid = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_paid']

# 3. Fines (Automated Tracking)
class Fine(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    fine_type = models.CharField(max_length=100)  # e.g., 'Late Payment', 'Missed Meeting'
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    date_issued = models.DateField(auto_now_add=True)
