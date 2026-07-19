from django.db import models
from django.contrib.auth.models import AbstractUser


# 1. Member Model (Constitution: Membership admission and identification)
class Member(AbstractUser):
    # We use Django's built-in User model for secure authentication
    phone_number = models.CharField(max_length=15)
    is_active_member = models.BooleanField(default=True)
    registration_date = models.DateField(auto_now_add=True)
    next_of_kin_name = models.CharField(max_length=100, blank=True)
    next_of_kin_phone = models.CharField(max_length=15, blank=True)
    guardian_1 = models.CharField(max_length=100, blank=True)
    guardian_2 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


# 2. Contributions (Constitution: Monthly contributions & AGM fees)
class Contribution(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Constitution: Monthly contributions (Ksh 1000) or AGM fee (Ksh 2000)
    contribution_type = models.CharField(max_length=50)
    date_paid = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_paid']


# 3. Fines (Constitution: Enforcing penalties for late payment or absence)
class Fine(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    fine_type = models.CharField(max_length=100)  # e.g., 'Late Payment', 'Non-attendance'
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    date_issued = models.DateField(auto_now_add=True)
