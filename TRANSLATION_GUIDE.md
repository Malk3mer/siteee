# نظام الترجمة الثنائي - Bilingual Translation System

## كيفية العمل - How It Works

تم تحديث الموقع بالكامل ليدعم التبديل السلس بين اللغة العربية والإنجليزية.

### اللغة الافتراضية - Default Language
- اللغة الافتراضية الآن: **الإنجليزية (English)**
- يمكن التبديل للعربية بضغطة زر واحدة

### كيفية إضافة نص جديد - How to Add New Text

#### للنصوص العادية - For Regular Text:
```html
<span data-ar="النص بالعربي" data-en="English Text">English Text</span>
```

#### للـ Placeholders:
```html
<input type="text" 
       placeholder="Search..." 
       data-ar-placeholder="ابحث..." 
       data-en-placeholder="Search...">
```

#### للـ Titles:
```html
<a href="#" 
   title="Click here" 
   data-ar-title="اضغط هنا" 
   data-en-title="Click here">Link</a>
```

### الملفات المحدثة - Updated Files

✅ base.html - القالب الأساسي
✅ home.html - الصفحة الرئيسية
✅ product_detail.html - تفاصيل المنتج
✅ cart.html - السلة
✅ create_order.html - إنشاء طلب
✅ wishlist.html - المفضلة
✅ login.html - تسجيل الدخول
✅ register.html - التسجيل
✅ translate.js - ملف الترجمة

### المميزات - Features

1. ✨ تبديل فوري بين اللغات بدون إعادة تحميل
2. 💾 حفظ اللغة المختارة في المتصفح
3. 🔄 تحديث تلقائي لجميع النصوص
4. 📱 دعم كامل للـ RTL و LTR
5. 🎯 سهولة الإضافة والتعديل

### زر تغيير اللغة - Language Toggle Button

الزر موجود في الـ Navbar:
- 🇬🇧 EN - للتبديل للإنجليزية
- 🇦🇪 AR - للتبديل للعربية

### ملاحظات مهمة - Important Notes

1. **النص الافتراضي**: يجب أن يكون النص داخل الـ tag هو النص الإنجليزي
2. **data-ar**: يحتوي على النص العربي
3. **data-en**: يحتوي على النص الإنجليزي
4. **اللغة المحفوظة**: يتم حفظها في localStorage

### مثال كامل - Complete Example

```html
<button class="btn">
    <span data-ar="اشتري الآن" data-en="Buy Now">Buy Now</span>
</button>
```

عند الضغط على زر اللغة:
- إذا كانت اللغة عربية → يظهر "اشتري الآن"
- إذا كانت اللغة إنجليزية → يظهر "Buy Now"

---

## للمطورين - For Developers

### إضافة صفحة جديدة - Adding New Page

1. أضف `data-ar` و `data-en` لكل نص
2. تأكد من أن النص الافتراضي إنجليزي
3. لا حاجة لأي كود JavaScript إضافي

### التخصيص - Customization

يمكنك تعديل ملف `translate.js` لإضافة مميزات إضافية مثل:
- ترجمة تلقائية من API
- دعم لغات إضافية
- تحميل الترجمات من ملف JSON

---

تم التحديث بنجاح! ✅
Updated Successfully! ✅
