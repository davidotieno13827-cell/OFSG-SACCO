import base64
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import RequestFactory, TestCase
from django.urls import reverse

from .models import Contribution, Fine, Member
from .views import dashboard, management_summary, members_list, member_detail


class RegistrationViewTests(TestCase):
    def test_registration_page_creates_a_new_member(self):
        response = self.client.post(reverse('register_member'), {
            'username': 'newmember',
            'email': 'newmember@example.com',
            'phone_number': '0755555555',
            'password': 'Secret123!',
            'confirm_password': 'Secret123!',
            'next_of_kin_name': 'Jane Doe',
            'next_of_kin_phone': '0766666666',
            'guardian_1': 'John Doe',
            'guardian_2': 'Mary Doe',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Member.objects.filter(username='newmember').exists())

    def test_member_registration_allows_file_uploads(self):
        png_data = base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8HwQACfsD' \
            'muxf+QAAAABJRU5ErkJggg=='
        )
        profile_picture = SimpleUploadedFile(
            'profile.png', png_data, content_type='image/png'
        )
        passport_photo = SimpleUploadedFile(
            'passport.png', png_data, content_type='image/png'
        )
        id_document = SimpleUploadedFile(
            'id_document.pdf', b'%PDF-1.4\n%EOF\n', content_type='application/pdf'
        )

        response = self.client.post(
            reverse('register_member'),
            {
                'username': 'filemember',
                'email': 'filemember@example.com',
                'phone_number': '0777777777',
                'password': 'Secret123!',
                'confirm_password': 'Secret123!',
                'next_of_kin_name': 'File Kin',
                'next_of_kin_phone': '0788888888',
                'guardian_1': 'File One',
                'guardian_2': 'File Two',
                'profile_picture': profile_picture,
                'passport_photo': passport_photo,
                'id_document': id_document,
            }
        )

        self.assertEqual(response.status_code, 302)
        member = Member.objects.get(username='filemember')
        self.assertTrue(member.profile_picture)
        self.assertTrue(member.passport_photo)
        self.assertTrue(member.id_document)

class DemoUserSeedTests(TestCase):
    def test_seed_demo_users_creates_demo_accounts(self):
        call_command('seed_demo_users')

        self.assertTrue(Member.objects.filter(username='admin').exists())
        self.assertTrue(Member.objects.filter(username='demo_member').exists())
        self.assertTrue(Member.objects.filter(username='demo_treasurer').exists())


class AuthenticationFlowTests(TestCase):
    def test_login_redirects_authenticated_user_to_dashboard(self):
        Member.objects.create_user(
            username='browseruser',
            email='browser@example.com',
            password='Secret123!',
            phone_number='0777777777',
            is_active=True,
        )

        response = self.client.post(
            reverse('login'),
            {'username': 'browseruser', 'password': 'Secret123!', 'next': '/members/dashboard/'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/members/dashboard/')


class MembersListViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = Member.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='securepass123',
            phone_number='0710000000',
        )

    def test_members_list_filters_by_search_and_status(self):
        Member.objects.create_user(
            username='alice',
            password='secret123',
            phone_number='0711111111',
            is_active_member=True,
        )
        Member.objects.create_user(
            username='bob',
            password='secret123',
            phone_number='0722222222',
            is_active_member=False,
        )

        request = self.factory.get(reverse('members_list'), {'search': 'ali', 'status': 'active'})
        request.user = self.user

        response = members_list(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'alice')
        self.assertNotContains(response, 'bob')

    def test_member_detail_page_shows_member_history(self):
        member = Member.objects.create_user(
            username='carol',
            password='secret123',
            phone_number='0733333333',
            is_active_member=True,
        )
        Contribution.objects.create(member=member, amount=2500, contribution_type='Monthly')
        Fine.objects.create(member=member, fine_type='Late Payment', amount=300, is_paid=False)

        request = self.factory.get(reverse('member_detail', args=[member.pk]))
        request.user = self.user

        response = member_detail(request, member.pk)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'carol')
        self.assertContains(response, 'Monthly')
        self.assertContains(response, 'Late Payment')

    def test_secure_member_file_endpoint_restricts_access(self):
        member = Member.objects.create_user(
            username='edward',
            password='secret123',
            phone_number='0755555555',
            is_active_member=True,
        )
        member.profile_picture.save('profile.jpg', SimpleUploadedFile('profile.jpg', b'fake_image', content_type='image/jpeg'))
        member.save()

        response = self.client.get(reverse('member_file', args=[member.pk, 'profile_picture']))
        self.assertEqual(response.status_code, 302)

        self.client.force_login(self.user)
        response = self.client.get(reverse('member_file', args=[member.pk, 'profile_picture']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'image/jpeg')
    def test_management_summary_page_lists_overview_metrics(self):
        member = Member.objects.create_user(
            username='dave',
            password='secret123',
            phone_number='0744444444',
            is_active_member=True,
        )
        Contribution.objects.create(member=member, amount=1000, contribution_type='Monthly')
        Fine.objects.create(member=member, fine_type='Late Payment', amount=200, is_paid=False)

        request = self.factory.get(reverse('management_summary'))
        request.user = self.user

        response = management_summary(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Management Summary')
        self.assertContains(response, 'Late Payment')

    def test_dashboard_shows_leader_controls_for_admin(self):
        request = self.factory.get(reverse('dashboard'))
        request.user = self.user

        response = dashboard(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Leader Control Center')
        self.assertContains(response, 'Member management')
        self.assertContains(response, 'Management summary')
        self.assertContains(response, 'Add contribution')
        self.assertContains(response, 'Issue fine')
