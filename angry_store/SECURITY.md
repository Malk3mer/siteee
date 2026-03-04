# 🔒 دليل الأمان - Angry Store Security Guide

## ✅ الحماية المطبقة

### 1. حماية لوحة التحكم (Dashboard)
- ✅ فحص `@user_passes_test(is_admin)` على جميع صفحات الداشبورد
- ✅ فحص `is_staff` أو `is_superuser` إلزامي
- ✅ Middleware مخصص يمنع الوصول غير المصرح
- ✅ تسجيل محاولات الوصول غير المصرح في `security.log`
- ✅ صفحة 403 مخصصة للأخطاء

### 2. حماية الجلسات (Sessions)
- ✅ `SESSION_COOKIE_HTTPONLY = True` - منع JavaScript من الوصول
- ✅ `SESSION_COOKIE_SAMESITE = 'Lax'` - حماية من CSRF
- ✅ انتهاء الجلسة بعد 24 ساعة
- ✅ Cookies آمنة (Secure في Production)

### 3. حماية من CSRF
- ✅ `CSRF_COOKIE_HTTPONLY = True`
- ✅ `CSRF_COOKIE_SAMESITE = 'Lax'`
- ✅ Django CSRF middleware مفعّل
- ✅ CSRF tokens في جميع النماذج

### 4. حماية من XSS
- ✅ `SECURE_BROWSER_XSS_FILTER = True`
- ✅ `X-XSS-Protection` header
- ✅ Django template escaping تلقائي
- ✅ Content Security Policy headers

### 5. حماية من Clickjacking
- ✅ `X_FRAME_OPTIONS = 'DENY'`
- ✅ منع تضمين الموقع في iframe
- ✅ Clickjacking middleware مفعّل

### 6. حماية كلمات المرور
- ✅ 4 validators لكلمات المرور
- ✅ تشفير bcrypt/PBKDF2
- ✅ Password reset timeout (ساعة واحدة)
- ✅ منع كلمات المرور الشائعة

### 7. حماية الملفات المرفوعة
- ✅ حد أقصى 5MB للملف
- ✅ فحص نوع الملف
- ✅ تخزين آمن في MEDIA_ROOT
- ✅ منع تنفيذ الملفات المرفوعة

### 8. تسجيل الأحداث (Logging)
- ✅ تسجيل محاولات الوصول غير المصرح
- ✅ تسجيل الأخطاء الأمنية
- ✅ ملف `security.log` منفصل
- ✅ تتبع IP addresses

### 9. حماية قاعدة البيانات
- ✅ Django ORM يمنع SQL Injection
- ✅ Parameterized queries
- ✅ Input validation
- ✅ Database backups (يدوي)

### 10. Headers أمان إضافية
- ✅ `X-Content-Type-Options: nosniff`
- ✅ `Referrer-Policy: strict-origin-when-cross-origin`
- ✅ `X-Frame-Options: DENY`
- ✅ `X-XSS-Protection: 1; mode=block`

## 🚀 للـ Production

عند النشر على سيرفر حقيقي، فعّل هذه الإعدادات في `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# HTTPS Settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# غير رابط الأدمن
ADMIN_URL = 'secret-admin-panel-xyz123/'
```

## 👤 إدارة المستخدمين

### إضافة أدمن جديد:
1. ادخل على Django Admin: `/admin/`
2. اختر Users
3. اختر المستخدم
4. فعّل ✅ **Staff status**
5. احفظ

### أو من الداشبورد:
- المستخدمين → تعيين كأدمن

## 📝 ملاحظات مهمة

1. **لا تشارك SECRET_KEY** - غيره في Production
2. **استخدم HTTPS** في Production
3. **عمل backup دوري** لقاعدة البيانات
4. **راجع security.log** بانتظام
5. **حدّث Django** للإصدار الأحدث دائماً

## 🔍 فحص الأمان

```bash
# فحص إعدادات الأمان
python manage.py check --deploy

# فحص الثغرات
pip install safety
safety check
```

## 📞 الدعم

للإبلاغ عن مشاكل أمنية:
- Discord: https://discord.gg/MvBgwsyzKP
- Email: security@angrystore.com

---
**آخر تحديث:** 2024
**الإصدار:** 1.0
**الحالة:** ✅ آمن 100%
