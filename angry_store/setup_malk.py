# -*- coding: utf-8 -*-
import os
import sys
import django

sys.stdout.reconfigure(encoding='utf-8')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

try:
    user = User.objects.get(username='malk')
    user.is_staff = True
    user.is_superuser = True
    user.set_password('malk20101512')
    user.save()
    print('User malk updated successfully!')
    print('Username: malk')
    print('Password: malk20101512')
    print('Is Staff:', user.is_staff)
    print('Is Superuser:', user.is_superuser)
except User.DoesNotExist:
    user = User.objects.create_superuser(
        username='malk',
        email='malk@angrystore.com',
        password='malk20101512'
    )
    print('User malk created successfully!')
    print('Username: malk')
    print('Password: malk20101512')
