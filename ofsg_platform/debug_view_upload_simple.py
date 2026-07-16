import os
import base64
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()

logging.getLogger('axes').setLevel(logging.CRITICAL)

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
        'username': 'simpleuser',
        'email': 'simple@example.com',
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
member = Member.objects.filter(username='simpleuser').first()
print('exists', bool(member))
if member:
    print('profile', repr(member.profile_picture), bool(member.profile_picture), member.profile_picture.name)
    print('passport', repr(member.passport_photo), bool(member.passport_photo), member.passport_photo.name)
    print('doc', repr(member.id_document), bool(member.id_document), member.id_document.name)
