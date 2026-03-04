# إضافة بيانات تجريبية للاختبار

## استخدام Django Shell

افتح Django shell:
```bash
python manage.py shell
```

ثم نفذ الأوامر التالية:

### 1. إنشاء مستخدم تجريبي

```python
from django.contrib.auth.models import User
from store.models import UserProfile

# إنشاء مستخدم عادي
user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123'
)

# إنشاء profile
UserProfile.objects.create(
    user=user,
    phone='01234567890'
)
```

### 2. إنشاء منتجات تجريبية

```python
from store.models import Product

# لعبة
Product.objects.create(
    name='God of War Ragnarök',
    description='لعبة أكشن ومغامرات ملحمية من سانتا مونيكا ستوديو',
    price=1200.00,
    product_type='game',
    is_active=True
)

Product.objects.create(
    name='Elden Ring',
    description='لعبة RPG من FromSoftware',
    price=1000.00,
    product_type='game',
    is_active=True
)

# اشتراك
Product.objects.create(
    name='Xbox Game Pass Ultimate',
    description='اشتراك شهري يتيح الوصول لمئات الألعاب',
    price=250.00,
    product_type='subscription',
    is_active=True
)

Product.objects.create(
    name='PlayStation Plus Premium',
    description='اشتراك بلايستيشن بلس بريميوم',
    price=300.00,
    product_type='subscription',
    is_active=True
)

# هاردوير
Product.objects.create(
    name='Logitech G502 HERO',
    description='ماوس جيمينج احترافي بـ 25600 DPI',
    price=800.00,
    product_type='hardware',
    is_active=True
)

Product.objects.create(
    name='HyperX Cloud II',
    description='سماعة جيمينج 7.1 محيطية',
    price=1500.00,
    product_type='hardware',
    is_active=True
)

Product.objects.create(
    name='Razer BlackWidow V3',
    description='كيبورد ميكانيكال RGB',
    price=2000.00,
    product_type='hardware',
    is_active=True
)

Product.objects.create(
    name='NVIDIA RTX 4070',
    description='كرت شاشة قوي للألعاب بدقة 4K',
    price=15000.00,
    product_type='hardware',
    is_active=True
)
```

### 3. إنشاء طلب تجريبي

```python
from store.models import Order

# احصل على مستخدم ومنتج
user = User.objects.first()
product = Product.objects.first()

# أنشئ طلب
Order.objects.create(
    user=user,
    product=product,
    payment_method='vodafone',
    discord_username='testuser#1234',
    whatsapp='01234567890',
    status='pending'
)
```

## أو استخدم Management Command

يمكنك إنشاء management command مخصص:

### إنشاء الملف:
`store/management/commands/populate_db.py`

```python
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Product, UserProfile

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        # إنشاء مستخدم تجريبي
        if not User.objects.filter(username='testuser').exists():
            user = User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
            UserProfile.objects.create(user=user, phone='01234567890')
            self.stdout.write(self.style.SUCCESS('Created test user'))

        # إنشاء منتجات
        products = [
            {
                'name': 'God of War Ragnarök',
                'description': 'لعبة أكشن ومغامرات ملحمية',
                'price': 1200.00,
                'product_type': 'game'
            },
            {
                'name': 'Xbox Game Pass Ultimate',
                'description': 'اشتراك شهري',
                'price': 250.00,
                'product_type': 'subscription'
            },
            {
                'name': 'Logitech G502 HERO',
                'description': 'ماوس جيمينج احترافي',
                'price': 800.00,
                'product_type': 'hardware'
            }
        ]

        for product_data in products:
            if not Product.objects.filter(name=product_data['name']).exists():
                Product.objects.create(**product_data)
                self.stdout.write(self.style.SUCCESS(f'Created {product_data["name"]}'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
```

### تشغيل الأمر:
```bash
python manage.py populate_db
```

## ملاحظات

⚠️ **تحذير:** هذه البيانات للاختبار فقط
⚠️ لا تستخدم في بيئة الإنتاج
⚠️ الصور يجب إضافتها يدوياً أو استخدام placeholder images

## Placeholder Images

يمكنك استخدام خدمات مثل:
- https://via.placeholder.com/300x200
- https://picsum.photos/300/200
- https://placehold.co/300x200

## مسح البيانات التجريبية

```python
# في Django shell
from store.models import Product, Order
from django.contrib.auth.models import User

# حذف جميع الطلبات
Order.objects.all().delete()

# حذف جميع المنتجات
Product.objects.all().delete()

# حذف المستخدمين التجريبيين (ما عدا الأدمن)
User.objects.filter(is_superuser=False).delete()
```
