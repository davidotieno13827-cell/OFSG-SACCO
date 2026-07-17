from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from members.models import Member


class Command(BaseCommand):
    help = 'Create demo users for the OFSG SACCO preview environment'

    def handle(self, *args, **options):
        treasurer_group, _ = Group.objects.get_or_create(name='Treasurer')

        admin_user, admin_created = Member.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'phone_number': '0710000000',
                'is_active': True,
                'is_staff': True,
                'is_superuser': True,
            },
        )
        admin_user.set_password('Admin123!')
        admin_user.is_active = True
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        demo_member, demo_member_created = Member.objects.get_or_create(
            username='demo_member',
            defaults={
                'email': 'demo.member@example.com',
                'phone_number': '0711111111',
                'is_active': True,
                'is_active_member': True,
                'next_of_kin_name': 'Grace Member',
                'next_of_kin_phone': '0722222222',
                'guardian_1': 'Ann Guardian',
                'guardian_2': 'Peter Guardian',
            },
        )
        demo_member.set_password('Demo123!')
        demo_member.is_active = True
        demo_member.is_active_member = True
        demo_member.save()

        demo_treasurer, demo_treasurer_created = Member.objects.get_or_create(
            username='demo_treasurer',
            defaults={
                'email': 'demo.treasurer@example.com',
                'phone_number': '0733333333',
                'is_active': True,
                'is_active_member': True,
            },
        )
        demo_treasurer.set_password('Demo123!')
        demo_treasurer.is_active = True
        demo_treasurer.is_active_member = True
        demo_treasurer.save()
        demo_treasurer.groups.add(treasurer_group)

        self.stdout.write(self.style.SUCCESS('Seeded demo users successfully.'))
        self.stdout.write('Admin: admin / Admin123!')
        self.stdout.write('Member: demo_member / Demo123!')
        self.stdout.write('Treasurer: demo_treasurer / Demo123!')
