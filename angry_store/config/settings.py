import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-angry-store-2024-change-in-production'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'store.middleware.SecurityMiddleware',  # Custom security middleware
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.cart_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Africa/Cairo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # غير هذا بإيميلك
EMAIL_HOST_PASSWORD = 'your-app-password'  # ضع App Password من Google
DEFAULT_FROM_EMAIL = 'Angry Store <your-email@gmail.com>'

# ===== SECURITY SETTINGS - إعدادات الأمان =====

# Session Security - أمان الجلسات
SESSION_COOKIE_SECURE = False  # True في Production مع HTTPS
SESSION_COOKIE_HTTPONLY = True  # منع JavaScript من الوصول للـ cookies
SESSION_COOKIE_SAMESITE = 'Lax'  # حماية من CSRF
SESSION_COOKIE_AGE = 86400  # 24 ساعة

# CSRF Protection - حماية من CSRF
CSRF_COOKIE_SECURE = False  # True في Production مع HTTPS
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_USE_SESSIONS = False
CSRF_COOKIE_AGE = 31449600  # سنة واحدة

# Security Headers - رؤوس الأمان
SECURE_BROWSER_XSS_FILTER = True  # حماية من XSS
SECURE_CONTENT_TYPE_NOSNIFF = True  # منع تخمين نوع المحتوى
X_FRAME_OPTIONS = 'DENY'  # منع تضمين الموقع في iframe

# Password Security - أمان كلمات المرور
PASSWORD_RESET_TIMEOUT = 3600  # ساعة واحدة لإعادة تعيين كلمة المرور

# Admin Security - أمان لوحة الإدارة
ADMIN_URL = 'admin/'  # غير هذا في Production لشيء صعب التخمين

# Rate Limiting - تحديد معدل الطلبات (يمكن إضافة django-ratelimit)
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB max upload
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

# Logging - تسجيل الأحداث
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'security.log',
        },
    },
    'loggers': {
        'django.security': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}

# للـ Production فقط - قم بتفعيل هذه الإعدادات عند النشر:
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
