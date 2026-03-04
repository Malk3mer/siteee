# -*- coding: utf-8 -*-
import os
import sys
import django

sys.stdout.reconfigure(encoding='utf-8')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import UserProfile, Product, Order

print('='*60)
print('  ANGRY STORE - System Check')
print('='*60)
print()

# Check admin user
print('1. Checking admin user (malk)...')
try:
    user = User.objects.get(username='malk')
    print(f'   ✓ User exists: {user.username}')
    print(f'   ✓ Is staff: {user.is_staff}')
    print(f'   ✓ Is superuser: {user.is_superuser}')
    print(f'   ✓ Email: {user.email}')
except User.DoesNotExist:
    print('   ✗ User malk not found!')
print()

# Check database tables
print('2. Checking database tables...')
print(f'   ✓ Users: {User.objects.count()}')
print(f'   ✓ User Profiles: {UserProfile.objects.count()}')
print(f'   ✓ Products: {Product.objects.count()}')
print(f'   ✓ Orders: {Order.objects.count()}')
print()

# Check media folders
print('3. Checking media folders...')
media_folders = ['media', 'media/products', 'media/payment_proofs']
for folder in media_folders:
    if os.path.exists(folder):
        print(f'   ✓ {folder} exists')
    else:
        print(f'   ✗ {folder} not found')
print()

print('='*60)
print('  System check completed!')
print('='*60)
print()
print('Login credentials:')
print('  Username: malk')
print('  Password: malk20101512')
print()
print('Start server: python manage.py runserver')
print('Or double-click: start.bat')
print()
