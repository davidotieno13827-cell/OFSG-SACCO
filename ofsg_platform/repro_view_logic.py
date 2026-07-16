import os
import base64

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()

from django.core.files.uploadedfile import SimpleUploadedFile
from members.forms import MemberRegistrationForm
from members.models import Member

png_data = base64.b64decode(
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8HwQACfsD' \
    'muxf+QAAAABJRU5ErkJggg=='
)

form = MemberRegistrationForm(
    data={
        'username': 'logicuser',
        'email': 'logic@example.com',
        'phone_number': '078',
        'password': 'Secret123!',
        'confirm_password': 'Secret123!',
        'next_of_kin_name': 'n',
        'next_of_kin_phone': '07',
        'guardian_1': 'g',
        'guardian_2': 'g2',
    },
    files={
        'profile_picture': SimpleUploadedFile('profile.png', png_data, content_type='image/png'),
        'passport_photo': SimpleUploadedFile('passport.png', png_data, content_type='image/png'),
        'id_document': SimpleUploadedFile('id_document.pdf', b'%PDF-1.4\n%EOF\n', content_type='application/pdf'),
    },
)
print('valid', form.is_valid())
print('errors', form.errors)
user = form.save()
for field_name in ('profile_picture', 'passport_photo', 'id_document'):
    uploaded_file = form.cleaned_data.get(field_name)
    if uploaded_file:
        setattr(user, field_name, uploaded_file)
user.save()
member = Member.objects.get(username='logicuser')
print('field values', member.profile_picture, member.passport_photo, member.id_document)
print('bools', bool(member.profile_picture), bool(member.passport_photo), bool(member.id_document))
print('names', member.profile_picture.name, member.passport_photo.name, member.id_document.name)
