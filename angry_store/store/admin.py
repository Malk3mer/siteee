from django.contrib import admin
from .models import UserProfile, Product, Order, Testimonial

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'product_type', 'platform', 'price', 'tags', 'is_active', 'created_at']
    list_filter = ['category', 'product_type', 'platform', 'is_active']
    search_fields = ['name', 'description', 'tags']
    list_editable = ['price', 'is_active']
    ordering = ['-created_at']
    
    fieldsets = (
        ('📝 Basic Information', {
            'fields': ('name', 'description', 'price', 'is_active')
        }),
        ('🎯 Category & Type', {
            'fields': ('category', 'product_type', 'platform'),
            'description': 'اختر القسم الذي سيظهر فيه المنتج (Offline Games, Online Games, Activate Games, etc.)'
        }),
        ('🏷️ Tags', {
            'fields': ('tags',),
            'description': 'أضف من 2 إلى 5 تاجات مفصولة بفاصلة. مثال: رائج, جديد, أكشن, رعب, متعدد اللاعبين'
        }),
        ('🖼️ Images & Video', {
            'fields': ('image', 'image_url', 'video_url'),
            'description': 'ارفع صورة أو ضع رابط صورة + رابط فيديو YouTube (اختياري)'
        }),
    )
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'tags':
            from django import forms
            kwargs['widget'] = forms.Textarea(attrs={
                'rows': 3, 
                'cols': 80, 
                'placeholder': 'مثال: رائج, جديد, أكشن, رعب, متعدد اللاعبين\n\nالتاجات المتاحة:\nرائج | جديد | عرض خاص | الأكثر مبيعاً | رعب | أكشن | مغامرات | رياضة | سباقات | استراتيجية | RPG | FPS | متعدد اللاعبين | لاعب واحد | عالم مفتوح | بقاء | محاكاة | ألغاز | قتال | مفتاح تفعيل | حساب كامل | اشتراك شهري | اشتراك سنوي | توصيل فوري | ضمان | أصلي | مستعمل | جديد بالكرتونة | كرت شاشة | معالج | رامات | هارد | SSD | ماوس | كيبورد | سماعة | شاشة | RGB | Gaming',
                'style': 'font-family: Arial; font-size: 13px;'
            })
        return super().formfield_for_dbfield(db_field, **kwargs)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'payment_method', 'status', 'created_at']
    list_filter = ['status', 'payment_method']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['username', 'text_preview', 'time_ago', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['username', 'text']
    list_editable = ['is_active']
    ordering = ['-created_at']
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'نص الرأي'
    
    fieldsets = (
        ('👤 معلومات العميل', {
            'fields': ('username', 'time_ago', 'avatar_color')
        }),
        ('💬 الرأي', {
            'fields': ('text', 'is_active')
        }),
    )
