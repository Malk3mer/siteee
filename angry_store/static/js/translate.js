// نظام ترجمة محسّن يدعم data-ar و data-en + ترجمة التاجات والميزات
(function() {
    // قاموس ترجمة شامل للتاجات والميزات
    const TAG_TRANSLATIONS = {
        // الميزات
        '⚡ توصيل فوري': '⚡ Instant Delivery',
        '✓ ضمان كامل': '✓ Full Warranty',
        '💎 جودة عالية': '💎 High Quality',
        '🔒 آمن 100%': '🔒 100% Safe',
        '📞 دعم 24/7': '📞 24/7 Support',
        '🚀 تسليم سريع': '🚀 Fast Delivery',
        '💯 أصلي': '💯 Original',
        '🎁 هدية مجانية': '🎁 Free Gift',
        '💳 دفع آمن': '💳 Secure Payment',
        '✨ مضمون': '✨ Guaranteed',
        '🎯 موثوق': '🎯 Trusted',
        '⭐ تقييم عالي': '⭐ High Rating',
        '🏅 معتمد': '🏅 Certified',
        '🔐 محمي': '🔐 Protected',
        '💪 قوي': '💪 Powerful',
        '🌟 ممتاز': '🌟 Excellent',
        '🔥 ساخن': '🔥 Hot',
        '⚡ فوري': '⚡ Instant',
        '✔️ مؤكد': '✔️ Confirmed',
        '🎁 عرض محدود': '🎁 Limited Offer',
        
        // التاجات الرئيسية
        '🔥 رائج': '🔥 Trending',
        '⭐ جديد': '⭐ New',
        '💎 عرض خاص': '💎 Special Offer',
        '🏆 الأكثر مبيعاً': '🏆 Best Seller',
        '👑 حصري': '👑 Exclusive',
        '💰 خصم': '💰 Discount',
        
        // أنواع الألعاب
        '👻 رعب': '👻 Horror',
        '⚔️ أكشن': '⚔️ Action',
        '🗺️ مغامرة': '🗺️ Adventure',
        '⚽ رياضة': '⚽ Sports',
        '🏎️ سباقات': '🏎️ Racing',
        '🎯 استراتيجية': '🎯 Strategy',
        '✈️ محاكاة': '✈️ Simulation',
        '🧩 ألغاز': '🧩 Puzzle',
        '🥊 قتال': '🥊 Fighting',
        '🏕️ بقاء': '🏕️ Survival',
        
        // طريقة اللعب
        '🎮 RPG': '🎮 RPG',
        '🔫 FPS': '🔫 FPS',
        '🎯 TPS': '🎯 TPS',
        '👥 متعدد اللاعبين': '👥 Multiplayer',
        '👤 لاعب واحد': '👤 Single Player',
        '🌍 عالم مفتوح': '🌍 Open World',
        '🤝 تعاوني': '🤝 Co-op',
        '🏅 تنافسي': '🏅 Competitive',
        '👊 معركة ملكية': '👊 Battle Royale',
        '📖 قصة غنية': '📖 Rich Story',
        
        // الرسومات
        '🎨 رسومات واقعية': '🎨 Realistic Graphics',
        '🕹️ بيكسل': '🕹️ Pixel Art',
        '🎭 رسوم متحركة': '🎭 Animated',
        '📐 2D': '📐 2D',
        '🎲 3D': '🎲 3D',
        '💎 4K': '💎 4K',
        '🥽 VR': '🥽 VR',
        '🎬 سينمائي': '🎬 Cinematic',
        
        // الأجواء
        '🐉 فانتازيا': '🐉 Fantasy',
        '🚀 خيال علمي': '🚀 Sci-Fi',
        '🧟 زومبي': '🧟 Zombie',
        '🌑 مظلم': '🌑 Dark',
        '🌈 ملون': '🌈 Colorful',
        '🎃 رعب نفسي': '🎃 Psychological Horror',
        
        // ميزات اللعبة
        '🏗️ بناء': '🏗️ Building',
        '⚒️ صناعة': '⚒️ Crafting',
        '🥷 تسلل': '🥷 Stealth',
        '🎖️ تكتيكي': '🎖️ Tactical',
        '⚡ سريع': '⚡ Fast-Paced',
        '😌 مسترخي': '😌 Relaxing',
        '🔥 صعب': '🔥 Difficult',
        '💊 إدمان': '💊 Addictive',
        '🎉 ممتع': '🎉 Fun',
        '🎵 موسيقى رائعة': '🎵 Great Music',
        
        // نوع المنتج والخدمات
        '🔑 مفتاح تفعيل': '🔑 Activation Key',
        '👤 حساب كامل': '👤 Full Account',
        '📅 اشتراك شهري': '📅 Monthly Subscription',
        '📆 اشتراك سنوي': '📆 Annual Subscription',
        '✅ ضمان': '✅ Warranty',
        '🔒 آمن': '🔒 Safe',
        '💸 سعر مميز': '💸 Special Price',
        '🎉 عرض اليوم': '🎉 Today\'s Deal',
        '⏰ عرض لفترة محدودة': '⏰ Limited Time Offer',
        '🎖️ موثق': '🎖️ Verified',
        
        // النسخ
        '📦 نسخة قياسية': '📦 Standard Edition',
        '💎 نسخة فاخرة': '💎 Deluxe Edition',
        '🏆 نسخة ذهبية': '🏆 Gold Edition',
        '👑 نسخة نهائية': '👑 Ultimate Edition',
        '📥 محتوى إضافي': '📥 DLC',
        '🆕 تحديث جديد': '🆕 New Update',
        '🔓 وصول مبكر': '🔓 Early Access',
        
        // هاردوير
        '♻️ مستعمل': '♻️ Used',
        '📦 جديد بالكرتونة': '📦 Brand New',
        '🎮 Gaming': '🎮 Gaming',
        '💡 RGB': '💡 RGB',
        '🖥️ كرت شاشة': '🖥️ Graphics Card',
        '⚙️ معالج': '⚙️ Processor',
        '💾 رامات': '💾 RAM',
        '💿 هارد': '💿 HDD',
        '⚡ SSD': '⚡ SSD',
        '🖱️ ماوس': '🖱️ Mouse',
        '⌨️ كيبورد': '⌨️ Keyboard',
        '🎧 سماعة': '🎧 Headset',
        '🖥️ شاشة': '🖥️ Monitor',
        '🎮 يد تحكم': '🎮 Controller',
        '🪑 كرسي جيمنج': '🪑 Gaming Chair',
        
        // منصات
        '💻 PC': '💻 PC',
        '🎮 PlayStation': '🎮 PlayStation',
        '🎮 Xbox': '🎮 Xbox',
        '🎮 Nintendo': '🎮 Nintendo',
        '📱 Mobile': '📱 Mobile',
        
        // إضافات
        '🌟 مميز': '🌟 Featured',
        '🔊 صوت محيطي': '🔊 Surround Sound',
        '🎬 قصة سينمائية': '🎬 Cinematic Story',
        '🏃 باركور': '🏃 Parkour',
        '🧙 سحر': '🧙 Magic',
        '🗡️ سيوف': '🗡️ Swords',
        '🏹 رماية': '🏹 Archery',
        '🛡️ دفاع': '🛡️ Defense',
        '🎪 كوميدي': '🎪 Comedy',
        '💔 درامي': '💔 Drama',
        '🛡️ حماية كاملة': '🛡️ Full Protection',
        '🎖️ مرخص': '🎖️ Licensed',
        '💼 احترافي': '💼 Professional',
        '🌐 عالمي': '🌐 Global',
        '📢 إعلان': '📢 Announcement',
        '📣 جديد اليوم': '📣 New Today',
        '🆕 وصل حديثاً': '🆕 Just Arrived',
        '🔴 مباشر': '🔴 Live',
        '⚠️ محدود': '⚠️ Limited',
        '🎁 مجاني': '🎁 Free',
        '💰 رخيص': '💰 Cheap',
        '💵 وفر': '💵 Save',
        '💴 خصم 50%': '💴 50% OFF',
        '💶 خصم 30%': '💶 30% OFF',
        '💷 خصم 20%': '💷 20% OFF'
    };
    
    function switchLanguage(lang) {
        const html = document.documentElement;
        html.setAttribute('lang', lang);
        html.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
        
        // تحديث جميع العناصر التي تحتوي على data-ar و data-en
        document.querySelectorAll('[data-ar][data-en]').forEach(el => {
            const text = lang === 'ar' ? el.getAttribute('data-ar') : el.getAttribute('data-en');
            if (text) {
                el.textContent = text;
            }
        });
        
        // تحديث التاجات (product-tag) والميزات (product-feature)
        document.querySelectorAll('.product-tag, .product-feature').forEach(tag => {
            const originalText = tag.getAttribute('data-original') || tag.textContent.trim();
            if (!tag.getAttribute('data-original')) {
                tag.setAttribute('data-original', originalText);
            }
            
            if (lang === 'en' && TAG_TRANSLATIONS[originalText]) {
                tag.textContent = TAG_TRANSLATIONS[originalText];
            } else if (lang === 'ar') {
                tag.textContent = originalText;
            }
        });
        
        // تحديث placeholders
        document.querySelectorAll('[data-ar-placeholder][data-en-placeholder]').forEach(el => {
            const placeholder = lang === 'ar' ? el.getAttribute('data-ar-placeholder') : el.getAttribute('data-en-placeholder');
            if (placeholder) {
                el.placeholder = placeholder;
            }
        });
        
        // تحديث titles
        document.querySelectorAll('[data-ar-title][data-en-title]').forEach(el => {
            const title = lang === 'ar' ? el.getAttribute('data-ar-title') : el.getAttribute('data-en-title');
            if (title) {
                el.title = title;
            }
        });
        
        // تحديث onclick للتأكيدات
        document.querySelectorAll('[data-ar-onclick][data-en-onclick]').forEach(el => {
            const onclick = lang === 'ar' ? el.getAttribute('data-ar-onclick') : el.getAttribute('data-en-onclick');
            if (onclick) {
                el.setAttribute('onclick', onclick);
            }
        });
        
        // تحديث زر اللغة
        const langIcon = document.getElementById('langIcon');
        const langText = document.getElementById('langText');
        if (langIcon) langIcon.textContent = lang === 'ar' ? '🇬🇧' : '🇦🇪';
        if (langText) langText.textContent = lang === 'ar' ? 'EN' : 'AR';
        
        // حفظ اللغة
        localStorage.setItem('language', lang);
    }
    
    window.toggleLanguage = function() {
        const currentLang = document.documentElement.getAttribute('lang') || 'en';
        const newLang = currentLang === 'ar' ? 'en' : 'ar';
        switchLanguage(newLang);
    };
    
    // تحميل اللغة المحفوظة عند بدء الصفحة
    window.addEventListener('DOMContentLoaded', () => {
        const savedLang = localStorage.getItem('language') || 'en';
        switchLanguage(savedLang);
    });
})();
