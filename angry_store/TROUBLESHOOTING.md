# 🔧 حل المشاكل الشائعة - Troubleshooting

## مشاكل التثبيت

### ❌ خطأ: "python is not recognized"
**الحل:**
- تأكد من تثبيت Python
- أضف Python إلى PATH
- أعد تشغيل Terminal

### ❌ خطأ: "pip is not recognized"
**الحل:**
```bash
python -m pip install --upgrade pip
```

### ❌ خطأ في تثبيت Pillow
**الحل:**
```bash
pip install --upgrade Pillow
# أو
pip install Pillow --no-cache-dir
```

## مشاكل قاعدة البيانات

### ❌ خطأ: "no such table"
**الحل:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### ❌ خطأ: "duplicate column name"
**الحل:**
```bash
# احذف ملفات migrations القديمة (ما عدا __init__.py)
# ثم:
python manage.py makemigrations
python manage.py migrate --fake
```

### ❌ خطأ: "database is locked"
**الحل:**
- أغلق جميع نوافذ Terminal
- احذف ملف `db.sqlite3.lock` إن وجد
- أعد تشغيل السيرفر

## مشاكل الصور والملفات

### ❌ الصور لا تظهر
**الحل:**
1. تأكد من وجود مجلد `media`
2. تأكد من الإعدادات في `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
3. تأكد من URLs في `config/urls.py`:
```python
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### ❌ خطأ عند رفع الصور
**الحل:**
```bash
# أنشئ المجلدات يدوياً
mkdir media
mkdir media\products
mkdir media\payment_proofs
```

## مشاكل CSS و JavaScript

### ❌ CSS لا يعمل
**الحل:**
1. تأكد من مسار الملف في `base.html`:
```html
<link rel="stylesheet" href="/static/css/style.css">
```
2. امسح cache المتصفح (Ctrl + Shift + Delete)
3. جرب:
```bash
python manage.py collectstatic
```

### ❌ JavaScript لا يعمل
**الحل:**
- افتح Console في المتصفح (F12)
- تحقق من الأخطاء
- تأكد من مسار الملف صحيح

## مشاكل تسجيل الدخول

### ❌ لا أستطيع تسجيل الدخول كأدمن
**الحل:**
```bash
# أنشئ حساب superuser جديد
python manage.py createsuperuser
```

### ❌ خطأ: "CSRF verification failed"
**الحل:**
- تأكد من وجود `{% csrf_token %}` في النموذج
- امسح cookies المتصفح
- تأكد من تفعيل CSRF middleware في settings.py

## مشاكل الصلاحيات

### ❌ لا أستطيع الوصول للوحة التحكم
**الحل:**
1. تأكد من تسجيل الدخول كأدمن
2. تأكد من صلاحيات المستخدم:
```python
# في Django shell
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(username='your_username')
>>> user.is_staff = True
>>> user.is_superuser = True
>>> user.save()
```

## مشاكل الأداء

### ❌ الموقع بطيء
**الحل:**
1. استخدم `select_related()` في queries
2. فعّل caching
3. قلل حجم الصور
4. استخدم PostgreSQL بدلاً من SQLite

### ❌ استهلاك عالي للذاكرة
**الحل:**
- قلل عدد المنتجات المعروضة في الصفحة
- استخدم pagination
- حسّن الصور

## مشاكل النشر

### ❌ خطأ 500 في الإنتاج
**الحل:**
1. فعّل DEBUG مؤقتاً لرؤية الخطأ
2. تحقق من logs
3. تأكد من:
   - ALLOWED_HOSTS صحيح
   - STATIC_ROOT محدد
   - قاعدة البيانات متصلة

### ❌ Static files لا تعمل في الإنتاج
**الحل:**
```bash
python manage.py collectstatic --noinput
```

## مشاكل الترميز (Encoding)

### ❌ النصوص العربية تظهر رموز غريبة
**الحل:**
1. تأكد من UTF-8 في جميع الملفات
2. في `settings.py`:
```python
LANGUAGE_CODE = 'ar'
```
3. في HTML:
```html
<meta charset="UTF-8">
```

## أوامر مفيدة للتشخيص

### فحص الإعدادات:
```bash
python manage.py check
```

### عرض migrations:
```bash
python manage.py showmigrations
```

### فتح Django shell:
```bash
python manage.py shell
```

### عرض URLs:
```bash
python manage.py show_urls  # يحتاج django-extensions
```

### مسح قاعدة البيانات وإعادة البناء:
```bash
# احذف db.sqlite3
del db.sqlite3
# احذف migrations (ما عدا __init__.py)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## الحصول على المساعدة

إذا لم تجد الحل:
1. تحقق من error message بالكامل
2. ابحث عن الخطأ في Google
3. راجع Django documentation
4. اسأل في Stack Overflow
5. افتح Issue على GitHub

## نصائح عامة

✅ احتفظ بنسخة احتياطية من قاعدة البيانات
✅ استخدم virtual environment دائماً
✅ اقرأ error messages بعناية
✅ جرب في بيئة تطوير قبل الإنتاج
✅ استخدم Git لتتبع التغييرات
