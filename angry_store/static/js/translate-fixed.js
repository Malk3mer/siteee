// نظام الترجمة الصحيح
(function() {
    const translations = {
        'الرئيسية': 'Home',
        'الألعاب': 'Games',
        'ألعاب أوفلاين': 'Offline Games',
        'ألعاب أونلاين': 'Online Games',
        'مفاتيح التفعيل': 'Activate Games',
        'الاشتراكات': 'Subscriptions',
        'نايترو': 'Nitro',
        'برامج': 'Software',
        'منصات مشاهدة': 'TV & Shows',
        'الهاردوير': 'Hardware',
        'قطع البيسي': 'PC Parts',
        'إكسسوارات': 'Accessories',
        'ملفي الشخصي': 'My Profile',
        'طلباتي': 'My Orders',
        'لوحة التحكم': 'Dashboard',
        'تسجيل الخروج': 'Logout',
        'تسجيل الدخول': 'Login',
        'تسجيل': 'Register',
        'السلة': 'Cart',
        'المفضلة': 'Wishlist',
        'ديسكورد': 'Discord',
        'جميع الروابط': 'All Links',
        'تواصل معنا': 'Contact Us',
        'جميع الحقوق محفوظة': 'All rights reserved'
    };

    function translateElement(element, toLang) {
        if (!element || element.tagName === 'SCRIPT' || element.tagName === 'STYLE') return;
        
        Array.from(element.childNodes).forEach(node => {
            if (node.nodeType === 3) { // Text node
                let text = node.textContent;
                const trimmed = text.trim();
                
                if (trimmed) {
                    Object.entries(translations).forEach(([ar, en]) => {
                        if (toLang === 'en' && trimmed === ar) {
                            node.textContent = text.replace(ar, en);
                        } else if (toLang === 'ar' && trimmed === en) {
                            node.textContent = text.replace(en, ar);
                        }
                    });
                    
                    // Currency
                    if (toLang === 'en') {
                        node.textContent = node.textContent.replace(/جنيه/g, 'EGP').replace(/\sج(?!\w)/g, ' EGP');
                    } else {
                        node.textContent = node.textContent.replace(/EGP/g, 'ج');
                    }
                }
            } else if (node.nodeType === 1) { // Element node
                translateElement(node, toLang);
            }
        });
    }

    window.toggleLanguage = function() {
        const html = document.documentElement;
        const isArabic = html.getAttribute('lang') === 'ar';
        const newLang = isArabic ? 'en' : 'ar';
        
        html.setAttribute('lang', newLang);
        html.setAttribute('dir', isArabic ? 'ltr' : 'rtl');
        
        const icon = document.getElementById('langIcon');
        const text = document.getElementById('langText');
        if (icon) icon.textContent = isArabic ? '🇦🇪' : '🇬🇧';
        if (text) text.textContent = isArabic ? 'AR' : 'EN';
        
        localStorage.setItem('language', newLang);
        translateElement(document.body, newLang);
    };

    window.addEventListener('DOMContentLoaded', () => {
        const saved = localStorage.getItem('language');
        if (saved === 'en') {
            document.documentElement.setAttribute('lang', 'en');
            document.documentElement.setAttribute('dir', 'ltr');
            const icon = document.getElementById('langIcon');
            const text = document.getElementById('langText');
            if (icon) icon.textContent = '🇦🇪';
            if (text) text.textContent = 'AR';
            translateElement(document.body, 'en');
        }
    });
})();
