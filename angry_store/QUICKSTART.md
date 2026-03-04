# تعليمات التشغيل السريع

## الخطوات:

1. افتح Terminal في مجلد المشروع

2. قم بتشغيل الأوامر التالية:

```bash
# إنشاء بيئة افتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
venv\Scripts\activate

# تثبيت المتطلبات
pip install -r requirements.txt

# إنشاء قاعدة البيانات
python manage.py makemigrations
python manage.py migrate

# إنشاء حساب أدمن
python manage.py createsuperuser

# تشغيل السيرفر
python manage.py runserver
```

3. افتح المتصفح على: http://127.0.0.1:8000

## ملاحظات مهمة:

- لتغيير أرقام الدفع: افتح ملف store/views.py وابحث عن payment_numbers
- لإضافة منتجات: سجل دخول كأدمن واذهب إلى /dashboard/products/add/
- لمراجعة الطلبات: اذهب إلى /dashboard/orders/

## حل المشاكل الشائعة:

### إذا ظهرت مشكلة في Pillow:
```bash
pip install --upgrade Pillow
```

### إذا لم تظهر الصور:
تأكد من إنشاء مجلد media في المشروع

### إذا لم يعمل CSS:
```bash
python manage.py collectstatic
```
