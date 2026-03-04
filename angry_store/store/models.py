from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    PRODUCT_TYPES = [
        ('game', 'لعبة رقمية'),
        ('subscription', 'اشتراك'),
        ('hardware', 'هاردوير'),
    ]
    
    CATEGORY_CHOICES = [
        ('offline_games', 'Offline Games'),
        ('online_games', 'Online Games'),
        ('game_keys', 'Activate Games'),
        ('nitro', 'Nitro'),
        ('software', 'Software'),
        ('streaming', 'Streaming'),
        ('pc_parts', 'PC Parts'),
        ('accessories', 'Accessories'),
    ]
    
    PLATFORM_CHOICES = [
        ('steam', 'Steam'),
        ('epic', 'Epic Games'),
        ('microsoft', 'Microsoft Store'),
        ('playstation', 'PlayStation'),
        ('xbox', 'Xbox'),
        ('origin', 'Origin'),
        ('uplay', 'Ubisoft Connect'),
        ('gog', 'GOG'),
        ('battle', 'Battle.net'),
        ('rockstar', 'Rockstar Games'),
        ('other', 'أخرى'),
    ]
    
    FEATURE_CHOICES = [
        ('⚡ توصيل فوري', '⚡ توصيل فوري'),
        ('✓  ', '✓  '),
        ('💎 جودة عالية', '💎 جودة عالية'),
        ('🔒 آمن 100%', '🔒 آمن 100%'),
        ('📞 دعم 24/7', '📞 دعم 24/7'),
        ('🚀 تسليم سريع', '🚀 تسليم سريع'),
        ('💯 أصلي', '💯 أصلي'),
        ('🎁 هدية مجانية', '🎁 هدية مجانية'),
        ('💳 دفع آمن', '💳 دفع آمن'),
        ('✨ مضمون', '✨ مضمون'),
        ('🎯 موثوق', '🎯 موثوق'),
        ('⭐ تقييم عالي', '⭐ تقييم عالي'),
        ('🏅 معتمد', '🏅 معتمد'),
        ('🔐 محمي', '🔐 محمي'),
        ('💪 قوي', '💪 قوي'),
        ('🌟 ممتاز', '🌟 ممتاز'),
        ('🔥 ساخن', '🔥 ساخن'),
        ('⚡ فوري', '⚡ فوري'),
        ('✔️ مؤكد', '✔️ مؤكد'),
        ('🎁 عرض محدود', '🎁 عرض محدود'),
    ]
    
    TAG_CHOICES = [
        # عربي - إنجليزي مع أيقونات
        ('🔥 رائج', '🔥 رائج'),
        ('⭐ جديد', '⭐ جديد'),
        ('💎 عرض خاص', '💎 عرض خاص'),
        ('🏆 الأكثر مبيعاً', '🏆 الأكثر مبيعاً'),
        ('👑 حصري', '👑 حصري'),
        ('💰 خصم', '💰 خصم'),
        
        # أنواع الألعاب
        ('👻 رعب', '👻 رعب'),
        ('⚔️ أكشن', '⚔️ أكشن'),
        ('🗺️ مغامرة', '🗺️ مغامرة'),
        ('⚽ رياضة', '⚽ رياضة'),
        ('🏎️ سباقات', '🏎️ سباقات'),
        ('🎯 استراتيجية', '🎯 استراتيجية'),
        ('✈️ محاكاة', '✈️ محاكاة'),
        ('🧩 ألغاز', '🧩 ألغاز'),
        ('🥊 قتال', '🥊 قتال'),
        ('🏕️ بقاء', '🏕️ بقاء'),
        
        # طريقة اللعب
        ('🎮 RPG', '🎮 RPG'),
        ('🔫 FPS', '🔫 FPS'),
        ('🎯 TPS', '🎯 TPS'),
        ('👥 متعدد اللاعبين', '👥 متعدد اللاعبين'),
        ('👤 لاعب واحد', '👤 لاعب واحد'),
        ('🌍 عالم مفتوح', '🌍 عالم مفتوح'),
        ('🤝 تعاوني', '🤝 تعاوني'),
        ('🏅 تنافسي', '🏅 تنافسي'),
        ('👊 معركة ملكية', '👊 معركة ملكية'),
        ('📖 قصة غنية', '📖 قصة غنية'),
        
        # الرسومات
        ('🎨 رسومات واقعية', '🎨 رسومات واقعية'),
        ('🕹️ بيكسل', '🕹️ بيكسل'),
        ('🎭 رسوم متحركة', '🎭 رسوم متحركة'),
        ('📐 2D', '📐 2D'),
        ('🎲 3D', '🎲 3D'),
        ('💎 4K', '💎 4K'),
        ('🥽 VR', '🥽 VR'),
        ('🎬 سينمائي', '🎬 سينمائي'),
        
        # الأجواء
        ('🐉 فانتازيا', '🐉 فانتازيا'),
        ('🚀 خيال علمي', '🚀 خيال علمي'),
        ('🧟 زومبي', '🧟 زومبي'),
        ('🌑 مظلم', '🌑 مظلم'),
        ('🌈 ملون', '🌈 ملون'),
        ('🎃 رعب نفسي', '🎃 رعب نفسي'),
        
        # ميزات اللعبة
        ('🏗️ بناء', '🏗️ بناء'),
        ('⚒️ صناعة', '⚒️ صناعة'),
        ('🥷 تسلل', '🥷 تسلل'),
        ('🎖️ تكتيكي', '🎖️ تكتيكي'),
        ('⚡ سريع', '⚡ سريع'),
        ('😌 مسترخي', '😌 مسترخي'),
        ('🔥 صعب', '🔥 صعب'),
        ('💊 إدمان', '💊 إدمان'),
        ('🎉 ممتع', '🎉 ممتع'),
        ('🎵 موسيقى رائعة', '🎵 موسيقى رائعة'),
        
        # نوع المنتج والخدمات
        ('🔑 مفتاح تفعيل', '🔑 مفتاح تفعيل'),
        ('👤 حساب كامل', '👤 حساب كامل'),
        ('📅 اشتراك شهري', '📅 اشتراك شهري'),
        ('📆 اشتراك سنوي', '📆 اشتراك سنوي'),
        ('⚡ توصيل فوري', '⚡ توصيل فوري'),
        ('✅ ضمان', '✅ ضمان'),
        ('💯 أصلي', '💯 أصلي'),
        ('🎁 هدية مجانية', '🎁 هدية مجانية'),
        ('🔒 آمن', '🔒 آمن'),
        ('💳 دفع آمن', '💳 دفع آمن'),
        ('📞 دعم 24/7', '📞 دعم 24/7'),
        ('🚀 تسليم سريع', '🚀 تسليم سريع'),
        ('✨ جودة عالية', '✨ جودة عالية'),
        ('🎯 موثوق', '🎯 موثوق'),
        ('💎 مضمون', '💎 مضمون'),
        ('🔐 محمي', '🔐 محمي'),
        ('⭐ تقييم عالي', '⭐ تقييم عالي'),
        ('🏅 معتمد', '🏅 معتمد'),
        ('🎖️ موثق', '🎖️ موثق'),
        ('💪 قوي', '💪 قوي'),
        ('🌟 ممتاز', '🌟 ممتاز'),
        ('🔥 ساخن', '🔥 ساخن'),
        ('⚡ فوري', '⚡ فوري'),
        ('✔️ مؤكد', '✔️ مؤكد'),
        ('🎁 عرض محدود', '🎁 عرض محدود'),
        ('💸 سعر مميز', '💸 سعر مميز'),
        ('🎉 عرض اليوم', '🎉 عرض اليوم'),
        ('⏰ عرض لفترة محدودة', '⏰ عرض لفترة محدودة'),
        
        # النسخ
        ('📦 نسخة قياسية', '📦 نسخة قياسية'),
        ('💎 نسخة فاخرة', '💎 نسخة فاخرة'),
        ('🏆 نسخة ذهبية', '🏆 نسخة ذهبية'),
        ('👑 نسخة نهائية', '👑 نسخة نهائية'),
        ('📥 محتوى إضافي', '📥 محتوى إضافي'),
        ('🆕 تحديث جديد', '🆕 تحديث جديد'),
        ('🔓 وصول مبكر', '🔓 وصول مبكر'),
        
        # هاردوير
        ('♻️ مستعمل', '♻️ مستعمل'),
        ('📦 جديد بالكرتونة', '📦 جديد بالكرتونة'),
        ('🎮 Gaming', '🎮 Gaming'),
        ('💡 RGB', '💡 RGB'),
        ('🖥️ كرت شاشة', '🖥️ كرت شاشة'),
        ('⚙️ معالج', '⚙️ معالج'),
        ('💾 رامات', '💾 رامات'),
        ('💿 هارد', '💿 هارد'),
        ('⚡ SSD', '⚡ SSD'),
        ('🖱️ ماوس', '🖱️ ماوس'),
        ('⌨️ كيبورد', '⌨️ كيبورد'),
        ('🎧 سماعة', '🎧 سماعة'),
        ('🖥️ شاشة', '🖥️ شاشة'),
        ('🎮 يد تحكم', '🎮 يد تحكم'),
        ('🪑 كرسي جيمنج', '🪑 كرسي جيمنج'),
        
        # منصات
        ('💻 PC', '💻 PC'),
        ('🎮 PlayStation', '🎮 PlayStation'),
        ('🎮 Xbox', '🎮 Xbox'),
        ('🎮 Nintendo', '🎮 Nintendo'),
        ('📱 Mobile', '📱 Mobile'),
        
        # إضافات
        ('🌟 مميز', '🌟 مميز'),
        ('🔊 صوت محيطي', '🔊 صوت محيطي'),
        ('🎬 قصة سينمائية', '🎬 قصة سينمائية'),
        ('🏃 باركور', '🏃 باركور'),
        ('🧙 سحر', '🧙 سحر'),
        ('🗡️ سيوف', '🗡️ سيوف'),
        ('🏹 رماية', '🏹 رماية'),
        ('🛡️ دفاع', '🛡️ دفاع'),
        ('🎪 كوميدي', '🎪 كوميدي'),
        ('💔 درامي', '💔 درامي'),
        ('🛡️ حماية كاملة', '🛡️ حماية كاملة'),
        ('🎖️ مرخص', '🎖️ مرخص'),
        ('💼 احترافي', '💼 احترافي'),
        ('🌐 عالمي', '🌐 عالمي'),
        ('📢 إعلان', '📢 إعلان'),
        ('📣 جديد اليوم', '📣 جديد اليوم'),
        ('🆕 وصل حديثاً', '🆕 وصل حديثاً'),
        ('🔴 مباشر', '🔴 مباشر'),
        ('⚠️ محدود', '⚠️ محدود'),
        ('🎁 مجاني', '🎁 مجاني'),
        ('💰 رخيص', '💰 رخيص'),
        ('💵 وفر', '💵 وفر'),
        ('💴 خصم 50%', '💴 خصم 50%'),
        ('💶 خصم 30%', '💶 خصم 30%'),
        ('💷 خصم 20%', '💷 خصم 20%'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='offline_games', help_text='اختر القسم الذي يظهر فيه المنتج')
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, blank=True, null=True, help_text='المنصة أو نوع المفتاح')
    tags = models.CharField(max_length=500, blank=True, help_text='اختر من 2 إلى 5 تاجات، افصل بينهم بفاصلة')
    features = models.CharField(max_length=300, blank=True, help_text='ميزات صغيرة تحت الوصف (مثل: توصيل فوري, ضمان)')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True, help_text='رابط الصورة (اختياري)')
    video_url = models.URLField(max_length=500, blank=True, null=True, help_text='رابط فيديو YouTube (اختياري)')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def get_image_url(self):
        if self.image_url:
            return self.image_url
        elif self.image:
            return self.image.url
        return '/static/images/placeholder.png'
    
    def get_tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []
    
    def get_features_list(self):
        if self.features:
            return [feature.strip() for feature in self.features.split(',')]
        return []
    
    def get_video_embed_url(self):
        if self.video_url:
            if 'youtube.com/watch?v=' in self.video_url:
                video_id = self.video_url.split('watch?v=')[1].split('&')[0]
                return f'https://www.youtube.com/embed/{video_id}'
            elif 'youtu.be/' in self.video_url:
                video_id = self.video_url.split('youtu.be/')[1].split('?')[0]
                return f'https://www.youtube.com/embed/{video_id}'
        return None

    def __str__(self):
        return self.name

class Order(models.Model):
    PAYMENT_METHODS = [
        ('vodafone', 'فودافون كاش'),
        ('instapay', 'InstaPay'),
        ('binance', 'Binance Pay'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'جاري استلام الطلب'),
        ('received', 'تم استلام الطلب'),
        ('processing', 'قيد التنفيذ'),
        ('completed', 'مكتمل'),
        ('rejected', 'مرفوض'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    discord_username = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    payment_proof = models.ImageField(upload_to='payment_proofs/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    class Meta:
        ordering = ['-created_at']


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    def get_total_price(self):
        return self.product.price * self.quantity

class Testimonial(models.Model):
    username = models.CharField(max_length=100, verbose_name='اسم العميل')
    text = models.TextField(verbose_name='نص الرأي')
    time_ago = models.CharField(max_length=50, default='منذ يومين', verbose_name='الوقت')
    avatar_color = models.CharField(max_length=100, default='linear-gradient(135deg, #5865F2, #7289DA)', verbose_name='لون الأفاتار')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='نشط')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'رأي عميل'
        verbose_name_plural = 'آراء العملاء'

    def __str__(self):
        return f"{self.username} - {self.text[:30]}"
