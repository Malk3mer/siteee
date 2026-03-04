# 📚 دليل المطور - Angry Store

## هيكل المشروع

```
angry_store/
├── config/              # إعدادات Django
│   ├── settings.py     # الإعدادات الرئيسية
│   ├── urls.py         # URLs الرئيسية
│   └── wsgi.py         # WSGI configuration
├── store/              # التطبيق الرئيسي
│   ├── models.py       # نماذج قاعدة البيانات
│   ├── views.py        # Views والمنطق
│   ├── forms.py        # نماذج الإدخال
│   ├── urls.py         # URLs التطبيق
│   ├── admin.py        # إعدادات لوحة الأدمن
│   └── signals.py      # Signals
├── templates/          # قوالب HTML
├── static/             # ملفات CSS/JS/Images
└── media/              # ملفات المستخدمين المرفوعة
```

## النماذج (Models)

### UserProfile
```python
- user: OneToOneField(User)
- phone: CharField(max_length=20)
- created_at: DateTimeField(auto_now_add=True)
```

### Product
```python
- name: CharField(max_length=200)
- description: TextField()
- price: DecimalField(max_digits=10, decimal_places=2)
- product_type: CharField(choices=['game', 'subscription', 'hardware'])
- image: ImageField(upload_to='products/')
- created_at: DateTimeField(auto_now_add=True)
- is_active: BooleanField(default=True)
```

### Order
```python
- user: ForeignKey(User)
- product: ForeignKey(Product)
- payment_method: CharField(choices=['vodafone', 'instapay', 'binance'])
- discord_username: CharField(max_length=100)
- whatsapp: CharField(max_length=20)
- payment_proof: ImageField(upload_to='payment_proofs/')
- status: CharField(choices=['pending', 'completed', 'rejected'])
- created_at: DateTimeField(auto_now_add=True)
- updated_at: DateTimeField(auto_now=True)
```

## URLs

### Public URLs
- `/` - الصفحة الرئيسية
- `/product/<id>/` - تفاصيل المنتج
- `/register/` - تسجيل حساب جديد
- `/login/` - تسجيل الدخول
- `/logout/` - تسجيل الخروج
- `/order/<product_id>/` - إنشاء طلب

### Dashboard URLs (Admin Only)
- `/dashboard/` - الإحصائيات
- `/dashboard/products/` - إدارة المنتجات
- `/dashboard/products/add/` - إضافة منتج
- `/dashboard/products/edit/<id>/` - تعديل منتج
- `/dashboard/products/delete/<id>/` - حذف منتج
- `/dashboard/users/` - إدارة المستخدمين
- `/dashboard/orders/` - إدارة الطلبات
- `/dashboard/orders/update/<id>/` - تحديث حالة الطلب

## Views الرئيسية

### home(request)
عرض جميع المنتجات مع إمكانية البحث والفلترة

### product_detail(request, pk)
عرض تفاصيل منتج معين

### register_view(request)
تسجيل مستخدم جديد

### login_view(request)
تسجيل الدخول

### create_order(request, product_id)
إنشاء طلب شراء جديد

### dashboard(request)
لوحة التحكم - الإحصائيات

## Forms

### RegisterForm
- username
- email
- phone
- password1
- password2

### OrderForm
- payment_method
- discord_username
- whatsapp
- payment_proof

### ProductForm
- name
- description
- price
- product_type
- image
- is_active

## Decorators المستخدمة

### @login_required
يتطلب تسجيل دخول المستخدم

### @user_passes_test(is_admin)
يتطلب صلاحيات أدمن

## إضافة ميزات جديدة

### إضافة نموذج جديد:
1. أضف النموذج في `models.py`
2. قم بعمل migrations: `python manage.py makemigrations`
3. طبق التغييرات: `python manage.py migrate`
4. سجل النموذج في `admin.py`

### إضافة صفحة جديدة:
1. أضف view في `views.py`
2. أضف URL في `urls.py`
3. أنشئ template في `templates/`

### إضافة طريقة دفع جديدة:
1. أضف الخيار في `models.py` في `PAYMENT_METHODS`
2. أضف الرقم في `views.py` في `payment_numbers`
3. قم بعمل migrations

## الأمان

### CSRF Protection
جميع النماذج محمية بـ CSRF token:
```html
{% csrf_token %}
```

### Password Hashing
Django يقوم بتشفير كلمات المرور تلقائياً

### File Upload Security
الصور يتم التحقق منها عبر Pillow

### SQL Injection Protection
Django ORM يحمي من SQL Injection تلقائياً

## التخصيص

### تغيير الألوان:
عدل `static/css/style.css` في `:root`

### تغيير أرقام الدفع:
عدل `store/views.py` في دالة `create_order`

### إضافة حقول للمستخدم:
عدل `UserProfile` في `models.py`

## الاختبارات

تشغيل الاختبارات:
```bash
python manage.py test
```

إضافة اختبار جديد في `store/tests.py`

## الأداء

### تحسين الاستعلامات:
استخدم `select_related()` و `prefetch_related()`

### Caching:
أضف Django cache framework للصفحات الثابتة

### Database Indexing:
أضف indexes للحقول المستخدمة في البحث

## المساهمة

1. Fork المشروع
2. أنشئ branch جديد
3. قم بالتعديلات
4. اختبر التعديلات
5. أرسل Pull Request

## الدعم الفني

للمساعدة أو الإبلاغ عن مشاكل، افتح Issue على GitHub
