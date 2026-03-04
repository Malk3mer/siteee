# 🚀 دليل الميزات الجديدة - Angry Store

## 📋 الميزات المضافة

### 1. 💬 Live Chat (Tawk.to)
### 2. 📦 تتبع الطلب المتقدم
### 3. 🌓 Dark/Light Mode
### 4. 🎥 فيديو المنتج (YouTube)
### 5. 📊 لوحة إحصائيات متقدمة
### 6. 📑 تقارير شهرية
### 7. 🔐 تسجيل دخول Google

---

## 1️⃣ Live Chat - Tawk.to 💬

### ما هو؟
شات مباشر مجاني يظهر في أسفل الصفحة للتواصل الفوري مع العملاء

### كيف تفعله؟

**الخطوة 1:** اذهب إلى https://www.tawk.to
**الخطوة 2:** سجل حساب مجاني
**الخطوة 3:** اضغط على "Add Property" وأضف موقعك
**الخطوة 4:** انسخ الكود من Dashboard
**الخطوة 5:** افتح ملف `base.html` وابحث عن:
```html
<!-- Tawk.to Live Chat -->
<script>
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/YOUR_PROPERTY_ID/YOUR_WIDGET_ID';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
</script>
```

**الخطوة 6:** استبدل `YOUR_PROPERTY_ID` و `YOUR_WIDGET_ID` بالكود الخاص بك

### المميزات:
- ✅ مجاني 100%
- ✅ تطبيق موبايل للرد
- ✅ إشعارات فورية
- ✅ حفظ المحادثات
- ✅ يعمل على كل الصفحات

---

## 2️⃣ تتبع الطلب المتقدم 📦

### ما هو؟
نظام تتبع مرئي يوضح مراحل الطلب بالتفصيل

### المراحل:
1. ✅ **تم استلام الطلب** - Order Received
2. ⏳ **جاري المراجعة** - Under Review  
3. ⏳ **جاري التحضير** - Processing
4. ✅ **تم الإرسال** - Shipped
5. ✅ **تم التسليم** - Delivered

### كيف تستخدمه؟

**من الداشبورد:**
1. اذهب إلى "الطلبات"
2. اختر طلب
3. غير الحالة من القائمة المنسدلة
4. احفظ

**العميل يشوف:**
- صفحة "طلباتي" تعرض كل الطلبات
- كل طلب له حالة ملونة
- تفاصيل كاملة عن كل مرحلة

### الألوان:
- 🟡 **Pending** - أصفر (قيد المراجعة)
- 🟢 **Completed** - أخضر (مكتمل)
- 🔴 **Rejected** - أحمر (مرفوض)

---

## 3️⃣ Dark/Light Mode 🌓

### ما هو؟
زر لتبديل بين الوضع الداكن والفاتح

### كيف يعمل؟
- زر 🌙/☀️ في أعلى الصفحة
- يحفظ اختيارك في المتصفح
- يطبق على كل الصفحات

### الاستخدام:
1. اضغط على زر القمر 🌙 للوضع الداكن
2. اضغط على زر الشمس ☀️ للوضع الفاتح
3. الاختيار يحفظ تلقائياً

### التخصيص:
افتح `static/css/dark-mode.css` لتعديل الألوان

---

## 4️⃣ فيديو المنتج 🎥

### ما هو؟
إضافة رابط فيديو YouTube لكل منتج

### كيف تضيفه؟

**من الداشبورد:**
1. اذهب إلى "المنتجات"
2. اضغط "إضافة منتج" أو "تعديل"
3. ابحث عن حقل "رابط الفيديو (YouTube)"
4. الصق رابط الفيديو
5. احفظ

**أمثلة روابط صحيحة:**
```
https://www.youtube.com/watch?v=VIDEO_ID
https://youtu.be/VIDEO_ID
```

### أين يظهر؟
- في صفحة تفاصيل المنتج
- تحت الصورة الرئيسية
- فيديو مدمج قابل للتشغيل

### ملاحظات:
- اختياري (مش لازم تحط فيديو لكل منتج)
- لو مفيش فيديو، مش هيظهر شيء
- يدعم YouTube فقط

---

## 5️⃣ لوحة إحصائيات متقدمة 📊

### ما هي؟
رسوم بيانية وإحصائيات في الداشبورد

### الإحصائيات المتوفرة:

#### 📈 المبيعات:
- إجمالي المبيعات (كل الوقت)
- مبيعات آخر 7 أيام
- مبيعات آخر 30 يوم
- رسم بياني للمبيعات اليومية

#### 📦 الطلبات:
- عدد الطلبات الكلي
- طلبات قيد المراجعة
- طلبات مكتملة
- طلبات مرفوضة

#### 👥 العملاء:
- عدد العملاء المسجلين
- عملاء جدد هذا الشهر
- أكثر العملاء شراءً

#### 🎮 المنتجات:
- أكثر 10 منتجات مبيعاً
- منتجات نفذت
- منتجات جديدة

### كيف تشوفها؟
1. سجل دخول كـ Admin
2. اذهب إلى الداشبورد
3. كل الإحصائيات في الصفحة الرئيسية

---

## 6️⃣ تقارير شهرية 📑

### ما هي؟
تقرير شامل عن أداء المتجر كل شهر

### محتوى التقرير:

#### 💰 المالية:
- إجمالي المبيعات
- متوسط قيمة الطلب
- أعلى يوم مبيعات

#### 📊 الطلبات:
- عدد الطلبات
- معدل التحويل
- نسبة الطلبات المكتملة

#### 🏆 أفضل 10:
- أكثر المنتجات مبيعاً
- أكثر الفئات طلباً
- أكثر العملاء شراءً

### كيف تحصل عليه؟

**طريقة 1 - تلقائي:**
- التقرير يُنشأ تلقائياً أول كل شهر
- يُحفظ في `reports/monthly/`

**طريقة 2 - يدوي:**
1. اذهب إلى الداشبورد
2. اضغط "تقارير"
3. اختر الشهر
4. اضغط "تحميل التقرير"

### صيغة التقرير:
- PDF - للطباعة
- Excel - للتحليل
- JSON - للبرمجة

---

## 7️⃣ تسجيل دخول Google 🔐

### ما هو؟
السماح للعملاء بتسجيل الدخول بحساب Google

### كيف تفعله؟

**الخطوة 1: إنشاء مشروع Google**
1. اذهب إلى https://console.cloud.google.com
2. اضغط "Create Project"
3. سمي المشروع "Angry Store"
4. اضغط "Create"

**الخطوة 2: تفعيل Google OAuth**
1. من القائمة الجانبية → "APIs & Services"
2. اضغط "Enable APIs and Services"
3. ابحث عن "Google+ API"
4. اضغط "Enable"

**الخطوة 3: إنشاء Credentials**
1. اذهب إلى "Credentials"
2. اضغط "Create Credentials" → "OAuth client ID"
3. اختر "Web application"
4. أضف:
   - Authorized JavaScript origins: `http://localhost:8000`
   - Authorized redirect URIs: `http://localhost:8000/accounts/google/login/callback/`
5. احفظ Client ID و Client Secret

**الخطوة 4: إضافة للموقع**
1. افتح `config/settings.py`
2. ابحث عن:
```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'YOUR_CLIENT_ID_HERE',
            'secret': 'YOUR_CLIENT_SECRET_HERE',
        }
    }
}
```
3. استبدل `YOUR_CLIENT_ID_HERE` و `YOUR_CLIENT_SECRET_HERE`

**الخطوة 5: تشغيل Migration**
```bash
python manage.py migrate
```

**الخطوة 6: إضافة Social App من Admin**
1. اذهب إلى `/admin`
2. اضغط "Social applications"
3. اضغط "Add social application"
4. املأ:
   - Provider: Google
   - Name: Google
   - Client id: (من Google Console)
   - Secret key: (من Google Console)
   - Sites: اختر موقعك
5. احفظ

### الاستخدام:
- زر "تسجيل دخول بـ Google" في صفحة Login
- زر "تسجيل بـ Google" في صفحة Register
- تسجيل دخول بضغطة واحدة

---

## 🔧 التثبيت الكامل

### 1. تثبيت المكتبات:
```bash
pip install django-allauth
pip install pillow
pip install reportlab
pip install openpyxl
```

### 2. تحديث settings.py:
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
```

### 3. تحديث urls.py:
```python
urlpatterns = [
    # ... الموجود
    path('accounts/', include('allauth.urls')),
]
```

### 4. تشغيل Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. إنشاء Superuser (لو مش موجود):
```bash
python manage.py createsuperuser
```

---

## 📝 ملاحظات مهمة

### Live Chat:
- ✅ مجاني للأبد
- ✅ بدون حد للرسائل
- ✅ تطبيق موبايل متاح

### Dark Mode:
- ✅ يحفظ الاختيار تلقائياً
- ✅ يعمل على كل الصفحات
- ✅ سلس وسريع

### فيديو المنتج:
- ⚠️ YouTube فقط
- ⚠️ اختياري (مش إجباري)
- ✅ يعمل على الموبايل

### Google Login:
- ⚠️ يحتاج إعداد Google Console
- ⚠️ للإنتاج: غير الروابط لدومين حقيقي
- ✅ آمن 100%

### التقارير:
- ✅ تلقائية كل شهر
- ✅ يمكن تحميلها يدوياً
- ✅ 3 صيغ متاحة

---

## 🆘 حل المشاكل

### Live Chat مش ظاهر؟
- تأكد من الكود صحيح
- تأكد من Property ID صحيح
- امسح الكاش وحدث الصفحة

### Dark Mode مش شغال؟
- تأكد من ملف `dark-mode.css` موجود
- تأكد من JavaScript شغال
- امسح الكاش

### Google Login مش شغال؟
- تأكد من Client ID صحيح
- تأكد من Redirect URI صحيح
- تأكد من Social App مضاف في Admin

### الفيديو مش ظاهر؟
- تأكد من الرابط صحيح
- تأكد من الفيديو عام (مش خاص)
- جرب رابط مختلف

---

## 📞 الدعم

لو عندك أي مشكلة:
1. راجع هذا الملف
2. تأكد من كل الخطوات
3. اسأل في Discord

---

## ✅ Checklist

قبل ما تشغل الموقع، تأكد من:

- [ ] تثبيت كل المكتبات
- [ ] تشغيل migrations
- [ ] إضافة Tawk.to code
- [ ] إعداد Google OAuth (لو عايز)
- [ ] تجربة Dark Mode
- [ ] إضافة فيديو لمنتج واحد للتجربة
- [ ] فحص الداشبورد والإحصائيات

---

**🎉 مبروك! كل الميزات جاهزة للاستخدام**
