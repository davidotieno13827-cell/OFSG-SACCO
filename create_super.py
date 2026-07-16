import os
import sys
sys.path.insert(0, r'C:\Users\Administrator\OneDrive\Desktop\OFSG SELF HELP GROUP\ofsg_platform')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from members.models import Member
username='admin'
email='admin@example.com'
password='AdminPass123'
if not Member.objects.filter(username=username).exists():
    Member.objects.create_superuser(username, email, password)
    print('superuser created')
else:
    print('superuser exists')
