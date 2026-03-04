// نظام الترجمة الشامل 100% - Auto Translation System
(function() {
    'use strict';
    
    // قاموس الترجمة الكامل
    const translations = {
        // Navbar & Navigation
        'الرئيسية': 'Home',
        'الألعاب': 'Games',
        'ألعاب أوفلاين': 'Offline Games',
        'ألعاب أونلاين': 'Online Games',
        'مفاتيح التفعيل': 'Activate Games',
        'الاشتراكات': 'Subscriptions',
        'اشتراكات': 'Subscriptions',
        'برامج': 'Software',
        'منصات مشاهدة': 'TV & Shows',
        'الهاردوير': 'Hardware',
        'هاردوير جيمنج': 'Gaming Hardware',
        'قطع البيسي': 'PC Parts',
        'إكسسوارات': 'Accessories',
        'نايترو': 'Nitro',
        'Nitro': 'نايترو',
        
        // User Menu
        'ملفي الشخصي': 'My Profile',
        'طلباتي': 'My Orders',
        'لوحة التحكم': 'Dashboard',
        'تسجيل الخروج': 'Logout',
        'تسجيل الدخول': 'Login',
        'تسجيل': 'Register',
        
        // Cart & Wishlist
        'سلة التسوق': 'Shopping Cart',
        'السلة': 'Cart',
        'المفضلة': 'Wishlist',
        'السلة فارغة': 'Cart is Empty',
        'المفضلة فارغة': 'Wishlist is Empty',
        'لم تقم بإضافة أي منتجات للسلة بعد': 'You haven\\'t added any products to cart yet',
        'لم تقم بإضافة أي منتجات للمفضلة بعد': 'You haven\\'t added any products to wishlist yet',
        'تصفح المنتجات': 'Browse Products',
        'الكمية': 'Qty',
        'الإجمالي': 'Total',
        'شراء جميع المنتجات': 'Buy All Products',
        'اشتري الآن': 'Buy Now',
        'حذف': 'Remove',
        'إضافة للسلة': 'Add to Cart',
        'إضافة للمفضلة': 'Add to Wishlist',
        'نقل للسلة': 'Move to Cart',
        
        // Product
        'المنتجات': 'Products',
        'جميع الألعاب': 'All Games',
        'عرض التفاصيل': 'View Details',
        'توصيل فوري': 'Instant Delivery',
        'ضمان': 'Warranty',
        ' ': 'Full Warranty',
        'دفع آمن': 'Secure Payment',
        'متوفر': 'Available',
        'غير متوفر': 'Out of Stock',
        'الفئة': 'Category',
        'المنصة': 'Platform',
        'الوسوم': 'Tags',
        'لا توجد منتجات متاحة حالياً': 'No products available',
        'السعر شامل الضريبة': 'Price includes tax',
        
        // Payment & Orders
        'إتمام الدفع': 'Complete Payment',
        'إتمام الطلب': 'Complete Order',
        'طريقة الدفع': 'Payment Method',
        'فودافون كاش': 'Vodafone Cash',
        'ارسل المبلغ إلى': 'Send amount to',
        'اسم حساب Discord': 'Discord Username',
        'رقم WhatsApp': 'WhatsApp Number',
        'صورة إثبات الدفع': 'Payment Proof',
        'إثبات الدفع': 'Payment Proof',
        'ارفع صورة إيصال الدفع': 'Upload payment receipt',
        'إرسال الطلب': 'Submit Order',
        'إرسال': 'Submit',
        'إلغاء': 'Cancel',
        'رقم الطلب': 'Order Number',
        'التاريخ': 'Date',
        'الحالة': 'Status',
        'قيد المراجعة': 'Pending',
        'مكتمل': 'Completed',
        'ملغي': 'Cancelled',
        'معلومات الطلب': 'Order Details',
        'معلومات الدفع': 'Payment Info',
        
        // Dashboard
        'الإحصائيات': 'Statistics',
        'إجمالي المستخدمين': 'Total Users',
        'إجمالي المنتجات': 'Total Products',
        'إجمالي الطلبات': 'Total Orders',
        'طلبات قيد المراجعة': 'Pending Orders',
        'المكاسب والإيرادات': 'Revenue & Earnings',
        'إجمالي المكسب': 'Total Revenue',
        'متوسط الطلب': 'Average Order',
        'طلبات مكتملة': 'Completed Orders',
        'معدل النجاح': 'Success Rate',
        'إشعارات وتنبيهات': 'Notifications & Alerts',
        'طلبات تحتاج مراجعة': 'Orders Need Review',
        'النظام يعمل بشكل جيد': 'System Running Well',
        'منتجات نشطة': 'Active Products',
        'إجراءات سريعة': 'Quick Actions',
        'إضافة منتج جديد': 'Add New Product',
        'مراجعة الطلبات': 'Review Orders',
        'إدارة المنتجات': 'Manage Products',
        'إدارة المستخدمين': 'Manage Users',
        'المستخدمين': 'Users',
        'الطلبات': 'Orders',
        'تعديل': 'Edit',
        'حذف المنتج': 'Delete',
        'اسم المنتج': 'Product Name',
        'الصورة': 'Image',
        'الإجراءات': 'Actions',
        'اسم المستخدم': 'Username',
        'البريد الإلكتروني': 'Email',
        'تاريخ التسجيل': 'Join Date',
        'الصلاحيات': 'Role',
        'مدير': 'Admin',
        'مستخدم': 'User',
        
        // Profile
        'الملف الشخصي': 'Profile',
        'معلومات الحساب': 'Account Information',
        'تغيير كلمة المرور': 'Change Password',
        'كلمة المرور الحالية': 'Current Password',
        'كلمة المرور الجديدة': 'New Password',
        'تأكيد كلمة المرور': 'Confirm Password',
        'حفظ التغييرات': 'Save Changes',
        'تحديث': 'Update',
        
        // Auth
        'تسجيل حساب جديد': 'Create New Account',
        'لديك حساب بالفعل؟': 'Already have an account?',
        'ليس لديك حساب؟': 'Don\\'t have an account?',
        'سجل الآن': 'Register Now',
        'كلمة المرور': 'Password',
        'تذكرني': 'Remember Me',
        'نسيت كلمة المرور؟': 'Forgot Password?',
        
        // Footer
        'ديسكورد': 'Discord',
        'جميع الروابط': 'All Links',
        'تواصل معنا': 'Contact Us',
        'جميع الحقوق محفوظة': 'All rights reserved',
        
        // Common
        'ابحث عن لعبتك المفضلة': 'Search for your favorite game',
        'ابحث عن لعبتك المفضلة...': 'Search for your favorite game...',
        'بحث': 'Search',
        'السعر': 'Price',
        'الوصف': 'Description',
        'التفاصيل': 'Details',
        'جنيه': 'EGP',
        'ج.م': 'EGP',
        'ج': 'EGP',
        'من': 'From',
        'إلى': 'To',
        'عرض الكل': 'View All',
        'المزيد': 'More',
        'رجوع': 'Back',
        'التالي': 'Next',
        'السابق': 'Previous',
        'تحميل': 'Loading',
        'لا توجد نتائج': 'No Results',
        'خطأ': 'Error',
        'نجح': 'Success',
        'تحذير': 'Warning',
        'معلومات': 'Info',
        
        // Hero Section
        'عروض حصرية لفترة محدودة': 'Exclusive Limited Time Offers',
        'اكتشف عالم الألعاب الرقمية': 'Discover the World of Digital Games',
        'آلاف الألعاب والاشتراكات الحصرية بأفضل الأسعار': 'Thousands of games and exclusive subscriptions at the best prices',
        'تسوق الآن': 'Shop Now',
        'انضم لديسكورد': 'Join Discord',
        'اشترك الآن': 'Subscribe Now',
        
        // Features
        'لماذا تختارنا': 'Why Choose Us',
        'لماذا تختارنا؟': 'Why Choose Us?',
        'أسعار تنافسية': 'Competitive Prices',
        'أفضل الأسعار في السوق': 'Best prices in the market',
        'دعم 24/7': 'Support 24/7',
        'فريق دعم متواجد طوال الوقت': 'Support team available all the time',
        'توصيل سريع': 'Fast Delivery',
        'استلم طلبك فوراً': 'Receive your order instantly',
        'احصل على منتجك فوراً بعد الدفع مباشرة': 'Get your product instantly after payment',
        'ضمان الجودة': 'Quality Guarantee',
        'منتجات أصلية 100%': '100% Original Products',
        
        // Reviews
        'آراء عملائنا': 'Customer Reviews',
        'التقييمات': 'Reviews',
        'تقييم': 'Rating',
        
        // Categories
        'الفئات': 'Categories',
        'الكل': 'All',
        'أكشن': 'Action',
        'مغامرات': 'Adventure',
        'رياضة': 'Sports',
        'سباقات': 'Racing',
        'استراتيجية': 'Strategy',
        'محاكاة': 'Simulation',
        
        // Additional translations
        'Discord': 'Discord',
        'WhatsApp': 'WhatsApp',
        'InstaPay': 'InstaPay',
        'Binance Pay': 'Binance Pay',
        'Cart': 'Cart',
        'Wishlist': 'Wishlist',
        'Login': 'Login',
        'Register': 'Register',
    };
    
    // دالة الترجمة الرئيسية
    function translatePage() {
        const isEnglish = document.documentElement.getAttribute('lang') === 'en';
        const direction = isEnglish ? 'en' : 'ar';
        
        // ترجمة جميع عناصر النص
        translateAllTextNodes(direction);
        
        // ترجمة الخصائص
        translateAttributes(direction);
        
        // ترجمة العملة
        translateCurrency(direction);
    }
    
    // ترجمة جميع عقد النص
    function translateAllTextNodes(direction) {
        const isToEnglish = direction === 'en';
        
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode: function(node) {
                    const parent = node.parentElement;
                    if (!parent || 
                        parent.tagName === 'SCRIPT' || 
                        parent.tagName === 'STYLE' ||
                        parent.hasAttribute('data-no-translate')) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    return node.textContent.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
                }
            }
        );
        
        const textNodes = [];
        while(walker.nextNode()) {
            textNodes.push(walker.currentNode);
        }
        
        textNodes.forEach(node => {
            let text = node.textContent;
            const originalText = text;
            
            if (isToEnglish) {
                // من العربية للإنجليزية
                Object.entries(translations).forEach(([ar, en]) => {
                    const regex = new RegExp(escapeRegex(ar), 'gi');
                    text = text.replace(regex, en);
                });
            } else {
                // من الإنجليزية للعربية
                Object.entries(translations).forEach(([ar, en]) => {
                    const regex = new RegExp(escapeRegex(en), 'gi');
                    text = text.replace(regex, ar);
                });
            }
            
            if (text !== originalText) {
                node.textContent = text;
            }
        });
    }
    
    // ترجمة الخصائص
    function translateAttributes(direction) {
        const isToEnglish = direction === 'en';
        const attributes = ['placeholder', 'title', 'alt', 'aria-label', 'data-ar', 'data-en'];
        
        document.querySelectorAll('[placeholder], [title], [alt], [aria-label], [data-ar], [data-en]').forEach(element => {
            attributes.forEach(attr => {
                if (element.hasAttribute(attr)) {
                    let value = element.getAttribute(attr);
                    const originalValue = value;
                    
                    if (isToEnglish) {
                        Object.entries(translations).forEach(([ar, en]) => {
                            value = value.replace(new RegExp(escapeRegex(ar), 'gi'), en);
                        });
                    } else {
                        Object.entries(translations).forEach(([ar, en]) => {
                            value = value.replace(new RegExp(escapeRegex(en), 'gi'), ar);
                        });
                    }
                    
                    if (value !== originalValue) {
                        element.setAttribute(attr, value);
                    }
                }
            });
        });
    }
    
    // ترجمة العملة
    function translateCurrency(direction) {
        const isToEnglish = direction === 'en';
        
        document.querySelectorAll('.currency, .product-price, [class*=\"price\"]').forEach(element => {
            let text = element.textContent;
            
            if (isToEnglish) {
                text = text.replace(/جنيه/gi, 'EGP')
                          .replace(/ج\\.م/gi, 'EGP')
                          .replace(/\\sج(?!\\w)/g, ' EGP');
            } else {
                text = text.replace(/EGP/gi, 'ج');
            }
            
            element.textContent = text;
        });
    }
    
    // دالة مساعدة لتجنب أحرف regex الخاصة
    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
    }
    
    // دالة تبديل اللغة
    window.toggleLanguage = function() {
        const html = document.documentElement;
        const currentLang = html.getAttribute('lang');
        const langIcon = document.getElementById('langIcon');
        const langText = document.getElementById('langText');
        
        if (currentLang === 'ar') {
            html.setAttribute('lang', 'en');
            html.setAttribute('dir', 'ltr');
            if (langIcon) langIcon.textContent = '🇦🇪';
            if (langText) langText.textContent = 'AR';
            localStorage.setItem('language', 'en');
        } else {
            html.setAttribute('lang', 'ar');
            html.setAttribute('dir', 'rtl');
            if (langIcon) langIcon.textContent = '🇬🇧';
            if (langText) langText.textContent = 'EN';
            localStorage.setItem('language', 'ar');
        }
        
        translatePage();
    };
    
    // تحميل اللغة المحفوظة عند بدء الصفحة
    window.addEventListener('DOMContentLoaded', function() {
        const savedLang = localStorage.getItem('language');
        if (savedLang === 'en') {
            const html = document.documentElement;
            html.setAttribute('lang', 'en');
            html.setAttribute('dir', 'ltr');
            const langIcon = document.getElementById('langIcon');
            const langText = document.getElementById('langText');
            if (langIcon) langIcon.textContent = '🇦🇪';
            if (langText) langText.textContent = 'AR';
            translatePage();
        }
    });
    
    // مراقبة التغييرات الديناميكية في الصفحة
    const observer = new MutationObserver(function(mutations) {
        const currentLang = document.documentElement.getAttribute('lang');
        if (currentLang === 'en') {
            mutations.forEach(function(mutation) {
                if (mutation.addedNodes.length) {
                    translatePage();
                }
            });
        }
    });
    
    // بدء المراقبة
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
})();
