# 📦 دليل تخصيص كروت المنتجات

## 🎯 الأجزاء الرئيسية للكرت

### 1️⃣ شبكة الكروت (Products Grid)
```css
.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    /* ☝️ 280px = الحد الأدنى لعرض الكرت */
    gap: 25px;  /* المسافة بين الكروت */
}
```
**للتعديل:**
- زود الرقم `280px` لكروت أعرض (مثلاً `320px`)
- قلل الرقم لكروت أضيق (مثلاً `250px`)

---

### 2️⃣ الكرت نفسه (Product Card)
```css
.product-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;  /* استدارة الزوايا */
    overflow: hidden;
}
```

---

### 3️⃣ صورة المنتج (Product Image) ⭐ الأهم
```css
.product-image {
    height: 340px;  /* 👈 ارتفاع الصورة - غير هذا الرقم */
    background: linear-gradient(135deg, var(--darker), var(--dark));
}
```
**للتعديل:**
- ✅ `340px` = ارتفاع متوسط (الحالي)
- ✅ `400px` = صورة أطول (لإظهار تفاصيل أكثر)
- ✅ `280px` = صورة أقصر
- ✅ `450px` = صورة طويلة جداً

---

### 4️⃣ معلومات المنتج (Product Info)
```css
.product-info {
    padding: 25px;  /* المسافة الداخلية */
}

.product-info h3 {
    font-size: 18px;      /* حجم اسم المنتج */
    min-height: 50px;     /* الحد الأدنى للارتفاع */
}

.product-description {
    font-size: 13px;      /* حجم الوصف */
    min-height: 42px;     /* الحد الأدنى للارتفاع */
}
```

---

### 5️⃣ السعر (Product Price)
```css
.product-price {
    font-size: 28px;  /* حجم السعر */
    font-weight: 900;
}
```

---

## 🎨 أمثلة سريعة للتعديل

### مثال 1: كروت أطول مع صور أكبر
```css
.products-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
}

.product-image {
    height: 420px;  /* صورة أطول */
}
```

### مثال 2: كروت أصغر ومضغوطة
```css
.products-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
}

.product-image {
    height: 280px;  /* صورة أقصر */
}

.product-info {
    padding: 18px;  /* مسافة أقل */
}
```

### مثال 3: كروت عريضة مع صور ضخمة
```css
.products-grid {
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
}

.product-image {
    height: 500px;  /* صورة طويلة جداً */
}
```

---

## 📱 التحكم في الموبايل

```css
@media (max-width: 768px) {
    .product-image {
        height: 250px;  /* صورة أقصر على الموبايل */
    }
}
```

---

## 🔧 التعديلات الموصى بها

| الهدف | التعديل |
|-------|---------|
| **إظهار الصورة بشكل أفضل** | زود `height` في `.product-image` |
| **كروت أعرض** | زود `minmax(280px)` في `.products-grid` |
| **كروت أضيق** | قلل `minmax(280px)` في `.products-grid` |
| **مسافة أكبر بين الكروت** | زود `gap` في `.products-grid` |
| **كرت أطول بالكامل** | زود `height` في `.product-image` |

---

## ⚡ نصائح مهمة

1. **لا تنسى** حفظ الملف بعد التعديل
2. **اعمل Refresh** للصفحة (Ctrl + F5)
3. **جرب أحجام مختلفة** حتى تحصل على الشكل المناسب
4. **احتفظ بنسخة احتياطية** قبل التعديلات الكبيرة

---

## 📍 مكان التعديل

الملف: `angry_store/static/css/style.css`

ابحث عن:
- `.products-grid` → للتحكم في عرض الكروت
- `.product-image` → للتحكم في ارتفاع الصورة
- `.product-info` → للتحكم في المحتوى

---

✨ **تم إنشاء هذا الدليل لمساعدتك في تخصيص الكروت بسهولة!**
