# -*- coding: utf-8 -*-
import os
import sys
import django

# Fix encoding for Windows
sys.stdout.reconfigure(encoding='utf-8')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import UserProfile

# Create user malk
if not User.objects.filter(username='malk').exists():
    user = User.objects.create_superuser(
        username='malk',
        email='malk@angrystore.com',
        password='malk20101512'
    )
    profile, created = UserProfile.objects.get_or_create(user=user)
    profile.phone = '01000000000'
    profile.save()
    print('User malk created successfully!')
    print('Username: malk')
    print('Password: malk20101512')
else:
    print('User malk already exists')
