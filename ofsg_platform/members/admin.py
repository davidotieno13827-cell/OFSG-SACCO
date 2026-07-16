from django.contrib import admin
from .models import Member, Contribution, Fine

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # This makes the admin list view clear and professional
    list_display = ('username', 'is_active_member', 'registration_date')
    list_filter = ('is_active_member',)
    search_fields = ('username', 'phone_number')

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    # This helps track monthly savings and AGM fees as required
    list_display = ('member', 'amount', 'contribution_type', 'date_paid')
    list_filter = ('contribution_type',)

@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    # Ensures penalties are visible for the Overseer/Executive to act on
    list_display = ('member', 'fine_type', 'amount', 'is_paid')
    list_filter = ('is_paid',)
