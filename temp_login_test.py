import os
import re
import sys
from urllib import request, parse
from http import cookiejar

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, 'ofsg_platform')
sys.path.insert(0, PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()
from members.models import Member

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'AdminPass123'
ADMIN_EMAIL = 'admin@example.com'
MEMBER_USERNAME = 'testmember'
MEMBER_PASSWORD = 'MemberPass123'
MEMBER_EMAIL = 'testmember@example.com'
BASE_URL = 'http://127.0.0.1:8001'

cj = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))

def get_csrf(url):
    html = opener.open(url).read().decode('utf-8', 'ignore')
    m = re.search(r'name=["\']csrfmiddlewaretoken["\'] value=["\']([^"\']+)["\']', html)
    if not m:
        raise RuntimeError('CSRF token not found on ' + url)
    return m.group(1)


def post(url, data, referer=None):
    data = parse.urlencode(data).encode('utf-8')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    if referer:
        headers['Referer'] = referer
    req = request.Request(url, data=data, headers=headers)
    return opener.open(req)


def ensure_member(username, password, email):
    user, created = Member.objects.get_or_create(username=username, defaults={'email': email, 'is_active': True})
    if created or not user.check_password(password):
        user.set_password(password)
        user.save()
        print(f'Created/updated member: {username}')
    return user


def ensure_admin(username, password, email):
    user, created = Member.objects.get_or_create(username=username, defaults={'email': email, 'is_active': True, 'is_staff': True, 'is_superuser': True})
    if created or not user.check_password(password) or not user.is_superuser or not user.is_staff:
        user.set_password(password)
        user.email = email
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f'Created/updated admin: {username}')
    return user


ensure_admin(ADMIN_USERNAME, ADMIN_PASSWORD, ADMIN_EMAIL)
ensure_member(MEMBER_USERNAME, MEMBER_PASSWORD, MEMBER_EMAIL)

print('Testing member login flow...')
login_url = BASE_URL + '/accounts/login/'
csrf = get_csrf(login_url)
resp = post(login_url, {
    'username': MEMBER_USERNAME,
    'password': MEMBER_PASSWORD,
    'csrfmiddlewaretoken': csrf,
    'next': '/members/dashboard/'
}, referer=login_url)
print('Member login response code:', resp.getcode())
print('Member login redirected to:', resp.geturl())

page = opener.open(BASE_URL + '/members/dashboard/')
print('Member dashboard code:', page.getcode())
html = page.read().decode('utf-8', 'ignore')
print('Member dashboard contains dashboard title:', 'dashboard' in html.lower())
profile_page = opener.open(BASE_URL + '/members/profile/')
print('Member profile page code:', profile_page.getcode())

print('\nTesting admin login flow...')
# Reset cookies for admin flow
cj = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
login_url = BASE_URL + '/admin/login/?next=/admin/'
csrf = get_csrf(login_url)
resp = post(login_url, {
    'username': ADMIN_USERNAME,
    'password': ADMIN_PASSWORD,
    'csrfmiddlewaretoken': csrf,
    'next': '/admin/'
}, referer=login_url)
print('Admin login response code:', resp.getcode())
print('Admin login redirected to:', resp.geturl())

page = opener.open(BASE_URL + '/admin/')
print('Admin index code:', page.getcode())
html = page.read().decode('utf-8', 'ignore')
print('Admin index contains Site administration:', 'site administration' in html.lower())

page = opener.open(BASE_URL + '/admin/members/member/')
print('Admin members changelist code:', page.getcode())
html = page.read().decode('utf-8', 'ignore')
print('Admin members changelist contains Select user to change:', 'select user to change' in html.lower())
