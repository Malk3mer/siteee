// نظام الترجمة البسيط والفعال
(function() {
    const translations = {
        'الرئيسية': 'Home', 'الألعاب': 'Games', 'ألعاب أوفلاين': 'Offline Games',
        'ألعاب أونلاين': 'Online Games', 'مفاتيح التفعيل': 'Activate Games',
        'الاشتراكات': 'Subscriptions', 'نايترو': 'Nitro', 'برامج': 'Software',
        'منصات مشاهدة': 'TV & Shows', 'الهاردوير': 'Hardware', 'قطع البيسي': 'PC Parts',
        'إكسسوارات': 'Accessories', 'ملفي الشخصي': 'My Profile', 'طلباتي': 'My Orders',
        'لوحة التحكم': 'Dashboard', 'تسجيل الخروج': 'Logout', 'تسجيل الدخول': 'Login',
        'تسجيل': 'Register', 'السلة': 'Cart', 'المفضلة': 'Wishlist', 'ديسكورد': 'Discord',
        'جميع الروابط': 'All Links', 'تواصل معنا': 'Contact Us',
        'جميع الحقوق محفوظة': 'All rights reserved', 'جنيه': 'EGP', 'ج': 'EGP'
    };

    window.toggleLanguage = function() {
        const html = document.documentElement;
        const isArabic = html.getAttribute('lang') === 'ar';
        
        html.setAttribute('lang', isArabic ? 'en' : 'ar');
        html.setAttribute('dir', isArabic ? 'ltr' : 'rtl');
        
        const icon = document.getElementById('langIcon');
        const text = document.getElementById('langText');
        if (icon) icon.textContent = isArabic ? '🇦🇪' : '🇬🇧';
        if (text) text.textContent = isArabic ? 'AR' : 'EN';
        
        localStorage.setItem('language', isArabic ? 'en' : 'ar');
        
        translateAll(isArabic ? 'en' : 'ar');
    };

    function translateAll(toLang) {
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
            acceptNode: n => n.parentElement.tagName !== 'SCRIPT' && n.parentElement.tagName !== 'STYLE' && n.textContent.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT
        });
        
        const nodes = [];
        while(walker.nextNode()) nodes.push(walker.currentNode);
        
        nodes.forEach(node => {
            let text = node.textContent;
            Object.entries(translations).forEach(([ar, en]) => {
                text = text.replace(new RegExp(ar.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), toLang === 'en' ? en : ar);
                text = text.replace(new RegExp(en.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), toLang === 'ar' ? ar : en);
            });
            if (toLang === 'en') {
                text = text.replace(/جنيه/g, 'EGP').replace(/\sج(?!\w)/g, ' EGP');
            } else {
                text = text.replace(/EGP/g, 'ج');
            }
            node.textContent = text;
        });
    }

    window.addEventListener('DOMContentLoaded', () => {
        if (localStorage.getItem('language') === 'en') {
            document.documentElement.setAttribute('lang', 'en');
            document.documentElement.setAttribute('dir', 'ltr');
            const icon = document.getElementById('langIcon');
            const text = document.getElementById('langText');
            if (icon) icon.textContent = '🇦🇪';
            if (text) text.textContent = 'AR';
            translateAll('en');
        }
    });
})();
