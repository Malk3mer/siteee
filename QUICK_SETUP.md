# 🚀 خطوات التنفيذ السريعة

## 1️⃣ تحديث قاعدة البيانات

```bash
cd angry_store
python manage.py makemigrations
python manage.py migrate
```

## 2️⃣ تفعيل Live Chat (Tawk.to)

1. اذهب إلى: https://www.tawk.to
2. سجل حساب مجاني
3. اضغط "Add Property"
4. انسخ الكود
5. افتح `templates/base.html`
6. ابحث عن:
```javascript
s1.src='https://embed.tawk.to/YOUR_PROPERTY_ID/YOUR_WIDGET_ID';
```
7. استبدل `YOUR_PROPERTY_ID` و `YOUR_WIDGET_ID` بالكود الخاص بك

## 3️⃣ تجربة الميزات

### Dark Mode:
- زر 🌙 في أسفل يمين الصفحة
- اضغط للتبديل بين الوضع الداكن والفاتح

### فيديو المنتج:
1. اذهب إلى `/admin`
2. افتح أي منتج
3. أضف رابط YouTube في حقل "video_url"
4. احفظ
5. افتح صفحة المنتج - الفيديو سيظهر

### Live Chat:
- سيظهر تلقائياً في أسفل يسار الصفحة
- يعمل على كل الصفحات

## 4️⃣ تسجيل دخول Google (اختياري)

### تثبيت المكتبة:
```bash
pip install django-allauth
```

### تحديث settings.py:
```python
INSTALLED_APPS = [
    # ... الموجود
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
```

### تحديث urls.py:
```python
from django.urls import path, include

urlpatterns = [
    # ... الموجود
    path('accounts/', include('allauth.urls')),
]
```

### تشغيل Migration:
```bash
python manage.py migrate
```

### إعداد Google Console:
1. https://console.cloud.google.com
2. Create Project
3. Enable Google+ API
4. Create OAuth Client ID
5. أضف:
   - Authorized JavaScript origins: `http://localhost:8000`
   - Authorized redirect URIs: `http://localhost:8000/accounts/google/login/callback/`

### إضافة Social App:
1. اذهب إلى `/admin`
2. Social applications → Add
3. املأ البيانات من Google Console
4. احفظ

## 5️⃣ الإحصائيات والتقارير

### الإحصائيات:
- موجودة في الداشبورد الرئيسي
- تظهر تلقائياً للـ Admin

### التقارير:
- ستضاف في تحديث قادم
- أو يمكن استخدام Django Admin لتصدير البيانات

## ✅ التحقق من التثبيت

```bash
# تشغيل السيرفر
python manage.py runserver

# افتح المتصفح
http://localhost:8000

# تحقق من:
# ✅ زر Dark Mode ظاهر
# ✅ Live Chat ظاهر (بعد إضافة الكود)
# ✅ يمكن إضافة فيديو للمنتج
```

## 📝 ملاحظات

- **Dark Mode**: يعمل فوراً بدون إعداد
- **Live Chat**: يحتاج حساب Tawk.to (مجاني)
- **فيديو المنتج**: يعمل فوراً بعد Migration
- **Google Login**: اختياري ويحتاج إعداد

## 🆘 مشاكل شائعة

### Migration Error:
```bash
python manage.py makemigrations store
python manage.py migrate store
```

### Static Files مش شغالة:
```bash
python manage.py collectstatic
```

### Dark Mode مش شغال:
- امسح الكاش: Ctrl+Shift+R
- تأكد من ملف `dark-mode.css` موجود

---

**🎉 كل شيء جاهز! استمتع بالميزات الجديدة**

راجع ملف `NEW_FEATURES_GUIDE.md` للشرح التفصيلي
