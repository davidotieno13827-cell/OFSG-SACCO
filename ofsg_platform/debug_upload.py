import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.getcwd())
import django
django.setup()
from django.core.files.uploadedfile import SimpleUploadedFile
from members.forms import MemberRegistrationForm
from PIL import Image
from io import BytesIO

buf = BytesIO()
img = Image.new('RGB', (1, 1), color='white')
img.save(buf, format='PNG')
png_data = buf.getvalue()
form = MemberRegistrationForm(
    data={
        'username': 'debuguser',
        'email': 'debuguser@example.com',
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
    }
)
print('valid', form.is_valid())
print('errors', form.errors)
print('profile', form.cleaned_data.get('profile_picture'))
print('passport', form.cleaned_data.get('passport_photo'))
print('id', form.cleaned_data.get('id_document'))
if form.is_valid():
    u = form.save()
    print('saved', u.pk, bool(u.profile_picture), bool(u.passport_photo), bool(u.id_document))
