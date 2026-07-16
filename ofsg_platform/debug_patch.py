import os
import base64

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()

from django.test import Client
from django.urls import reverse
from members.models import Member
from django.core.files.uploadedfile import SimpleUploadedFile
import members.views as views
from members.forms import MemberRegistrationForm

orig_save = MemberRegistrationForm.save

def patched_save(self, commit=True):
    user = orig_save(self, commit=commit)
    print('patched save returned', user, user.profile_picture, user.passport_photo, user.id_document)
    return user

MemberRegistrationForm.save = patched_save

png_data = base64.b64decode(
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8HwQACfsD' \
    'muxf+QAAAABJRU5ErkJggg=='
)

client = Client()
response = client.post(
    reverse('register_member'),
    {
        'username': 'patcheduser',
        'email': 'patched@example.com',
        'phone_number': '0777777777',
        'password': 'Secret123!',
        'confirm_password': 'Secret123!',
        'next_of_kin_name': 'File Kin',
        'next_of_kin_phone': '0788888888',
        'guardian_1': 'File One',
        'guardian_2': 'File Two',
    },
    files={
        'profile_picture': SimpleUploadedFile('profile.png', png_data, content_type='image/png'),
        'passport_photo': SimpleUploadedFile('passport.png', png_data, content_type='image/png'),
        'id_document': SimpleUploadedFile('id_document.pdf', b'%PDF-1.4\n%EOF\n', content_type='application/pdf'),
    },
)
print('status', response.status_code)
member = Member.objects.get(username='patcheduser')
print('member fields', member.profile_picture, member.passport_photo, member.id_document)
