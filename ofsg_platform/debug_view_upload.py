import os
import base64

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()

from django.test import Client
from django.urls import reverse
from members.models import Member
from django.core.files.uploadedfile import SimpleUploadedFile

png_data = base64.b64decode(
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8HwQACfsD' \
    'muxf+QAAAABJRU5ErkJggg=='
)

client = Client()
response = client.post(
    reverse('register_member'),
    {
        'username': 'debugfilemember',
        'email': 'debugfilemember@example.com',
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
member = Member.objects.get(username='debugfilemember')
print('profile field raw', repr(member.profile_picture))
print('profile bool', bool(member.profile_picture))
print('profile name', member.profile_picture.name)
print('passport field raw', repr(member.passport_photo))
print('passport bool', bool(member.passport_photo))
print('doc field raw', repr(member.id_document))
print('doc bool', bool(member.id_document))
print('member dict', member.__dict__.get('profile_picture'), member.__dict__.get('passport_photo'), member.__dict__.get('id_document'))
