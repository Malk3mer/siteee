import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

templates_dir = r'c:\Users\sg716\OneDrive\Desktop\siteee\angry_store\templates\dashboard'

files_to_fix = [
    'add_product.html',
    'add_testimonial.html',
    'change_password.html',
    'dashboard.html',
    'edit_product.html',
    'orders.html',
    'products.html',
    'testimonials.html',
    'users.html'
]

for filename in files_to_fix:
    filepath = os.path.join(templates_dir, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '{% load static %}' not in content:
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

print('\nAll dashboard files have been fixed!')
