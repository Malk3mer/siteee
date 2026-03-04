#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكريبت لتحديث جميع ملفات HTML بإضافة data-ar و data-en
"""

import os
import re

# قاموس الترجمة الشامل
TRANSLATIONS = {
    # الصفحات والعناوين
    'ألعاب أوفلاين': 'Offline Games',
    'ألعاب أونلاين': 'Online Games',
    'مفاتيح التفعيل': 'Activation Keys',
    'تفعيلات واشتراكات': 'Subscriptions',
    'نايترو': 'Nitro',
    'برامج': 'Software',
    'منصات مشاهدة': 'Streaming',
    'هاردوير جيمنج': 'Gaming Hardware',
    'قطع البيسي': 'PC Parts',
    'إكسسوارات': 'Accessories',
    
    # النصوص العامة
    'أفضل الألعاب الرقمية بأسعار منافسة • توصيل فوري': 'Best digital games • Instant delivery',
    'ابحث عن لعبتك المفضلة...': 'Search for your favorite game...',
    'ابحث عن الاشتراك...': 'Search for subscription...',
    'ابحث عن برنامج...': 'Search for software...',
    'ابحث عن اشتراك...': 'Search for subscription...',
    'ابحث عن المنتج...': 'Search for product...',
    'ابحث عن قطعة...': 'Search for part...',
    'ابحث عن إكسسوار...': 'Search for accessory...',
    'ابحث عن اشتراك نايترو...': 'Search for Nitro subscription...',
    
    # الأزرار
    'بحث': 'Search',
    'عرض التفاصيل': 'View Details',
    'إضافة للسلة': 'Add to Cart',
    'إضافة للمفضلة': 'Add to Wishlist',
    
    # الرسائل
    'لا توجد ألعاب متاحة حالياً': 'No games available',
    'لا توجد منتجات متاحة حالياً': 'No products available',
    'لا توجد اشتراكات متاحة حالياً': 'No subscriptions available',
    'لا توجد برامج متاحة حالياً': 'No software available',
    'لا توجد منتجات هاردوير متاحة حالياً': 'No hardware available',
    'لا توجد قطع متاحة حالياً': 'No parts available',
    'لا توجد إكسسوارات متاحة حالياً': 'No accessories available',
    'لا توجد اشتراكات نايترو متاحة حالياً': 'No Nitro subscriptions available',
    'تحقق لاحقاً للحصول على عروض جديدة!': 'Check back soon for new releases!',
    
    # الأوصاف
    'مفاتيح تفعيل أصلية • اشتراكات مميزة • توصيل فوري': 'Original activation keys • Premium subscriptions • Instant delivery',
    'اشتراكات Discord Nitro • توصيل فوري • أفضل الأسعار': 'Discord Nitro subscriptions • Instant delivery • Best prices',
    'برامج أصلية • مفاتيح تفعيل • توصيل فوري': 'Original software • Activation keys • Instant delivery',
    'Netflix • Shahid • OSN • اشتراكات مميزة': 'Netflix • Shahid • OSN • Premium subscriptions',
    'أفضل معدات الألعاب • جودة عالية • أسعار منافسة': 'Best gaming equipment • High quality • Competitive prices',
    'كروت شاشة • معالجات • رامات • SSD': 'Graphics cards • Processors • RAM • SSD',
    'ماوس • كيبورد • سماعات • شاشات': 'Mouse • Keyboard • Headsets • Monitors',
    
    # العملة والأسعار
    'ج': 'EGP',
    'جنيه': 'EGP',
    'السعر شامل الضريبة': 'Price includes tax',
    
    # الميزات
    'توصيل فوري': 'Instant Delivery',
    'ضمان': 'Warranty',
    'دعم 24/7': '24/7 Support',
    
    # Dashboard
    'لوحة التحكم': 'Dashboard',
    'الإحصائيات': 'Statistics',
    'المنتجات': 'Products',
    'المستخدمين': 'Users',
    'الطلبات': 'Orders',
    'إضافة منتج': 'Add Product',
    'تعديل منتج': 'Edit Product',
    'حذف': 'Delete',
    'تعديل': 'Edit',
    'حفظ': 'Save',
    'إلغاء': 'Cancel',
}

def wrap_text_with_translation(text, ar_text, en_text):
    """يضيف data-ar و data-en للنص"""
    return f'<span data-ar="{ar_text}" data-en="{en_text}">{en_text}</span>'

def update_html_file(filepath):
    """يحدث ملف HTML واحد"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # تحديث النصوص
        for ar_text, en_text in TRANSLATIONS.items():
            # تحديث النصوص العادية
            pattern = f'>{ar_text}<'
            replacement = f'>{wrap_text_with_translation("", ar_text, en_text)}<'
            content = content.replace(pattern, replacement)
            
            # تحديث placeholders
            pattern = f'placeholder="{ar_text}"'
            replacement = f'placeholder="{en_text}" data-ar-placeholder="{ar_text}" data-en-placeholder="{en_text}"'
            content = content.replace(pattern, replacement)
            
            # تحديث titles
            pattern = f'title="{ar_text}"'
            replacement = f'title="{en_text}" data-ar-title="{ar_text}" data-en-title="{en_text}"'
            content = content.replace(pattern, replacement)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ تم تحديث: {filepath}")
        return True
    except Exception as e:
        print(f"❌ خطأ في {filepath}: {e}")
        return False

def main():
    """الدالة الرئيسية"""
    templates_dir = 'angry_store/templates'
    
    # قائمة الملفات المراد تحديثها
    files_to_update = [
        'offline_games.html',
        'online_games.html',
        'activate_games.html',
        'subscriptions.html',
        'nitro.html',
        'software.html',
        'streaming.html',
        'hardware.html',
        'pc_parts.html',
        'accessories.html',
    ]
    
    updated = 0
    for filename in files_to_update:
        filepath = os.path.join(templates_dir, filename)
        if os.path.exists(filepath):
            if update_html_file(filepath):
                updated += 1
    
    print(f"\n✅ تم تحديث {updated} ملف بنجاح!")

if __name__ == '__main__':
    main()
