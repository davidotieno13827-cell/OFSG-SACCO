import os
import sys
from pathlib import Path
# Ensure project root is on sys.path so `config` can be imported
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from members.models import Member
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

username = 'testuser'
email = 'testuser@example.com'
password = 'Testpass123!'

user = None
if not Member.objects.filter(username=username).exists():
    user = Member.objects.create_user(username=username, email=email, password=password)
    user.is_active = False
    user.save()
    print('Created user:', username)
else:
    user = Member.objects.get(username=username)
    print('User already exists:', username)

uid = urlsafe_base64_encode(force_bytes(user.pk))
token = default_token_generator.make_token(user)
print('Activation URL: http://127.0.0.1:8000/members/activate/{}/{}'.format(uid, token))
