import os
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from django.test import Client
from members.models import Member
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

username = 'testuser'
try:
    user = Member.objects.get(username=username)
except Member.DoesNotExist:
    print('Test user not found; run create_test_user.py first')
    sys.exit(1)

uid = urlsafe_base64_encode(force_bytes(user.pk))
token = default_token_generator.make_token(user)
activation_path = f'/members/activate/{uid}/{token}/'
client = Client()
response = client.get(activation_path)
print('GET', activation_path, '->', response.status_code)
# Reload user
user.refresh_from_db()
print('User is_active:', user.is_active)
