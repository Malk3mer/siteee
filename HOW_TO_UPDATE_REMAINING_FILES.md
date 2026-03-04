# 🚀 دليل سريع لتحديث الملفات المتبقية

## 📝 الملفات المتبقية (18 ملف):

### 1. ملفات الألعاب (9 ملفات):
- online_games.html
- activate_games.html
- subscriptions.html
- nitro.html
- software.html
- streaming.html
- hardware.html
- pc_parts.html
- accessories.html

### 2. ملفات Dashboard (9 ملفات):
- dashboard/dashboard.html
- dashboard/products.html
- dashboard/add_product.html
- dashboard/edit_product.html
- dashboard/orders.html
- dashboard/users.html
- dashboard/testimonials.html
- dashboard/add_testimonial.html
- dashboard/change_password.html

---

## ⚡ الطريقة السريعة (3 خطوات):

### الخطوة 1: افتح الملف
```bash
# مثال
code angry_store/templates/online_games.html
```

### الخطوة 2: ابحث عن النصوص العربية
استخدم Ctrl+F وابحث عن:
- `>النص العربي<`
- `placeholder="النص العربي"`
- `title="النص العربي"`

### الخطوة 3: استبدل بالنمط الجديد

#### للنصوص العادية:
```html
<!-- قبل -->
<h1>ألعاب أونلاين</h1>

<!-- بعد -->
<h1><span data-ar="ألعاب أونلاين" data-en="Online Games">Online Games</span></h1>
```

#### للـ Placeholders:
```html
<!-- قبل -->
<input placeholder="ابحث...">

<!-- بعد -->
<input placeholder="Search..." 
       data-ar-placeholder="ابحث..." 
       data-en-placeholder="Search...">
```

---

## 📋 قائمة الترجمات الجاهزة:

### الصفحات:
```
ألعاب أونلاين → Online Games
مفاتيح التفعيل → Activation Keys
الاشتراكات → Subscriptions
نايترو → Nitro
برامج → Software
منصات مشاهدة → Streaming
هاردوير جيمنج → Gaming Hardware
قطع البيسي → PC Parts
إكسسوارات → Accessories
```

### Dashboard:
```
لوحة التحكم → Dashboard
الإحصائيات → Statistics
المنتجات → Products
إضافة منتج → Add Product
تعديل منتج → Edit Product
الطلبات → Orders
المستخدمين → Users
الشهادات → Testimonials
إضافة شهادة → Add Testimonial
تغيير كلمة المرور → Change Password
```

### الأزرار:
```
بحث → Search
حفظ → Save
إلغاء → Cancel
حذف → Delete
تعديل → Edit
إضافة → Add
عرض → View
تحديث → Update
```

### الحالات:
```
قيد المراجعة → Pending
مكتمل → Completed
مرفوض → Rejected
نشط → Active
غير نشط → Inactive
```

### الرسائل:
```
لا توجد بيانات → No data
تم الحفظ بنجاح → Saved successfully
حدث خطأ → An error occurred
هل أنت متأكد؟ → Are you sure?
```

---

## 🎯 مثال كامل (online_games.html):

### قبل:
```html
<h1>ألعاب أونلاين</h1>
<p>أفضل الألعاب الأونلاين</p>
<input placeholder="ابحث عن لعبة...">
<button>بحث</button>
```

### بعد:
```html
<h1><span data-ar="ألعاب أونلاين" data-en="Online Games">Online Games</span></h1>
<p><span data-ar="أفضل الألعاب الأونلاين" data-en="Best online games">Best online games</span></p>
<input placeholder="Search for game..." 
       data-ar-placeholder="ابحث عن لعبة..." 
       data-en-placeholder="Search for game...">
<button><span data-ar="بحث" data-en="Search">Search</span></button>
```

---

## 💡 نصائح سريعة:

### ✅ افعل:
1. ✅ ابدأ بملف واحد في كل مرة
2. ✅ استخدم Find & Replace (Ctrl+H)
3. ✅ اختبر الملف بعد التحديث
4. ✅ احفظ نسخة احتياطية

### ❌ لا تفعل:
1. ❌ لا تحدث كل الملفات مرة واحدة
2. ❌ لا تنسى النص الإنجليزي
3. ❌ لا تضع النص العربي كافتراضي

---

## 🔧 استخدام Find & Replace:

### في VS Code:
1. اضغط `Ctrl+H`
2. في "Find": `>ألعاب أونلاين<`
3. في "Replace": `><span data-ar="ألعاب أونلاين" data-en="Online Games">Online Games</span><`
4. اضغط "Replace All"

---

## ⏱️ الوقت المتوقع:

- **ملف واحد:** 5-10 دقائق
- **9 ملفات ألعاب:** 1-1.5 ساعة
- **9 ملفات Dashboard:** 1-1.5 ساعة
- **المجموع:** 2-3 ساعات

---

## ✅ قائمة التحقق:

بعد تحديث كل ملف:
- [ ] جميع النصوص العربية تم استبدالها
- [ ] جميع Placeholders تم تحديثها
- [ ] جميع Titles تم تحديثها
- [ ] النص الافتراضي إنجليزي
- [ ] تم اختبار الملف
- [ ] لا توجد أخطاء

---

## 🎉 النتيجة المتوقعة:

بعد تحديث جميع الملفات:
- ✅ **30 ملف** محدث بالكامل
- ✅ **200+ نص** مترجم
- ✅ **100%** من الموقع ثنائي اللغة
- ✅ **0 نص عربي** في الكود الافتراضي
- ✅ **موقع احترافي** بالكامل

---

## 📞 إذا واجهت مشكلة:

1. راجع الملفات المحدثة كمثال
2. راجع `COMPLETE_TRANSLATION_GUIDE.md`
3. تأكد من صحة النمط
4. اختبر في المتصفح

---

**ابدأ الآن! 🚀**

الملفات الأساسية جاهزة، والباقي سهل!
