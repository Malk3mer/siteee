import os
import re
import sys

# إصلاح مشكلة encoding في Windows
sys.stdout.reconfigure(encoding='utf-8')

# مسار مجلد templates
templates_dir = r'c:\Users\sg716\OneDrive\Desktop\siteee\angry_store\templates'

# قائمة الملفات التي يجب إصلاحها
files_to_fix = [
    'accessories.html',
    'activate_games.html',
    'create_order.html',
    'games.html',
    'hardware.html',
    'my_orders.html',
    'nitro.html',
    'offline_games.html',
    'online_games.html',
    'pc_parts.html',
    'software.html',
    'streaming.html',
    'subscriptions.html'
]

for filename in files_to_fix:
    filepath = os.path.join(templates_dir, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # التحقق إذا كان الملف يحتوي على {% load static %} بالفعل
        if '{% load static %}' not in content:
            # إضافة {% load static %} بعد {% extends 'base.html' %}
            if "{% extends 'base.html' %}" in content:
                content = content.replace(
                    "{% extends 'base.html' %}",
                    "{% extends 'base.html' %}\n{% load static %}"
                )
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f'Fixed: {filename}')
            else:
                print(f'Warning: No extends found in: {filename}')
        else:
            print(f'Already updated: {filename}')
    else:
        print(f'File not found: {filename}')

print('\nAll files have been fixed!')
