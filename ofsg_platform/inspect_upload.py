import os
import base64

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()

from django.core.files.uploadedfile import SimpleUploadedFile
from members.forms import MemberRegistrationForm

png_data = base64.b64decode(
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8HwQACfsD' \
    'muxf+QAAAABJRU5ErkJggg=='
)

f = SimpleUploadedFile('profile.png', png_data, content_type='image/png')
form = MemberRegistrationForm(
    data={
        'username': 'uniqueuser',
        'email': 'unique@example.com',
        'phone_number': '078',
        'password': 'Secret123!',
        'confirm_password': 'Secret123!',
        'next_of_kin_name': 'n',
        'next_of_kin_phone': '07',
        'guardian_1': 'g',
        'guardian_2': 'g2',
    },
    files={
        'profile_picture': f,
        'passport_photo': f,
        'id_document': SimpleUploadedFile('id_document.pdf', b'%PDF-1.4\n%EOF\n', content_type='application/pdf'),
    },
)
print('valid', form.is_valid())
print('errors', form.errors)
if form.is_valid():
    user = form.save()
    print('profile object', user.profile_picture, repr(user.profile_picture))
    print('bool', bool(user.profile_picture))
    print('name', user.profile_picture.name)
    print('instance dict', user.__dict__.get('profile_picture'))
    saved = user.__class__.objects.get(pk=user.pk)
    print('db value', saved.profile_picture, repr(saved.profile_picture))
    print('db bool', bool(saved.profile_picture))
    print('db name', saved.profile_picture.name)
