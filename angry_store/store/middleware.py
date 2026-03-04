"""
Security Middleware - حماية إضافية للموقع
"""
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
import logging

logger = logging.getLogger('django.security')

class SecurityMiddleware:
    """Middleware للحماية الإضافية"""
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # فحص محاولات الوصول للداشبورد
        if request.path.startswith('/dashboard/'):
            if not request.user.is_authenticated:
                messages.error(request, '⛔ يجب تسجيل الدخول أولاً')
                logger.warning(f'Unauthorized dashboard access attempt from IP: {self.get_client_ip(request)}')
                return redirect('login')
            
            if not (request.user.is_staff or request.user.is_superuser):
                messages.error(request, '⛔ ليس لديك صلاحية للوصول إلى لوحة التحكم')
                logger.warning(f'Non-admin user {request.user.username} tried to access dashboard')
                return redirect('home')
        
        response = self.get_response(request)
        
        # إضافة رؤوس أمان إضافية
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        return response
    
    def get_client_ip(self, request):
        """الحصول على IP الحقيقي للمستخدم"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
