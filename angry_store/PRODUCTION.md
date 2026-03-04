# إعدادات الإنتاج (Production Settings)

## قبل النشر على السيرفر:

### 1. تغيير SECRET_KEY
في ملف `config/settings.py`:
```python
SECRET_KEY = 'your-new-secret-key-here'  # استخدم مفتاح عشوائي قوي
```

### 2. تعطيل DEBUG
```python
DEBUG = False
```

### 3. تحديد ALLOWED_HOSTS
```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

### 4. إعداد قاعدة بيانات PostgreSQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'angry_store_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. إعداد الملفات الثابتة
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

ثم قم بتشغيل:
```bash
python manage.py collectstatic
```

### 6. إعداد HTTPS
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### 7. إعداد البريد الإلكتروني (اختياري)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## خوادم النشر الموصى بها:

1. **Heroku** - سهل للمبتدئين
2. **DigitalOcean** - مرن وقوي
3. **AWS** - للمشاريع الكبيرة
4. **PythonAnywhere** - مجاني للبداية

## أوامر مهمة للإنتاج:

```bash
# جمع الملفات الثابتة
python manage.py collectstatic --noinput

# إنشاء قاعدة البيانات
python manage.py migrate

# إنشاء حساب أدمن
python manage.py createsuperuser
```

## استخدام Gunicorn (موصى به):

```bash
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## استخدام Nginx (موصى به):

قم بإنشاء ملف تكوين Nginx:
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /static/ {
        alias /path/to/angry_store/staticfiles/;
    }

    location /media/ {
        alias /path/to/angry_store/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
