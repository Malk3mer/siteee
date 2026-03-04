from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q, Count
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, Order, UserProfile, Testimonial
from .forms import RegisterForm, OrderForm, ProductForm, ChangePasswordForm

def is_admin(user):
    """فحص صارم: فقط المستخدمين الذين تم تعيينهم كـ staff أو superuser"""
    return user.is_authenticated and (user.is_staff or user.is_superuser)

def home(request):
    # عرض جميع الألعاب (أوفلاين وأونلاين)
    products = Product.objects.filter(
        is_active=True,
        category__in=['offline_games', 'online_games', 'game_keys']
    )
    
    product_type = request.GET.get('type')
    search = request.GET.get('search')
    
    if product_type:
        products = products.filter(product_type=product_type)
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    
    testimonials = Testimonial.objects.filter(is_active=True)
    
    return render(request, 'home.html', {'products': products, 'testimonials': testimonials})

def games_page(request):
    products = Product.objects.filter(is_active=True, product_type='game')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'games.html', {'products': products})

def offline_games(request):
    products = Product.objects.filter(is_active=True, category='offline_games')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'offline_games.html', {'products': products})

def online_games(request):
    products = Product.objects.filter(is_active=True, category='online_games')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'online_games.html', {'products': products})

def activate_games(request):
    products = Product.objects.filter(is_active=True, category='game_keys')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'activate_games.html', {'products': products})

def subscriptions_page(request):
    products = Product.objects.filter(is_active=True, product_type='subscription')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'subscriptions.html', {'products': products})

def hardware_page(request):
    products = Product.objects.filter(is_active=True, product_type='hardware')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'hardware.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, phone=form.cleaned_data['phone'])
            login(request, user)
            messages.success(request, 'تم إنشاء الحساب بنجاح!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_order(request, product_id):
    from .models import Cart
    product = get_object_or_404(Product, pk=product_id)
    
    # Get cart items for display
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    total = sum(item.get_total_price() for item in cart_items) if cart_items.exists() else product.price
    
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            # If coming from cart, create orders for all items
            if cart_items.exists():
                payment_method = request.POST.get('payment_method')
                discord_username = request.POST.get('discord_username')
                whatsapp = request.POST.get('whatsapp')
                payment_proof = request.FILES.get('payment_proof')
                
                # Create order for each item with quantity
                for item in cart_items:
                    for _ in range(item.quantity):
                        Order.objects.create(
                            user=request.user,
                            product=item.product,
                            payment_method=payment_method,
                            discord_username=discord_username,
                            whatsapp=whatsapp,
                            payment_proof=payment_proof
                        )
                # Clear cart
                cart_items.delete()
                messages.success(request, 'تم إرسال طلباتك بنجاح! سيتم مراجعتها قريباً')
            else:
                # Single product order
                order = form.save(commit=False)
                order.user = request.user
                order.product = product
                order.save()
                messages.success(request, 'تم إرسال طلبك بنجاح! سيتم مراجعته قريباً')
            return redirect('my_orders')
    else:
        form = OrderForm()
    
    payment_numbers = {
        'vodafone': '01007875534',
        'instapay': '01222755348',
        'binance': 'angrystore@binance.com'
    }
    
    return render(request, 'create_order.html', {
        'form': form,
        'product': product,
        'cart_items': cart_items,
        'total': total,
        'payment_numbers': payment_numbers
    })

@user_passes_test(is_admin)
def dashboard(request):
    total_users = UserProfile.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status='pending').count()
    completed_orders = Order.objects.filter(status='completed').count()
    rejected_orders = Order.objects.filter(status='rejected').count()
    
    # حساب المكاسب الحقيقية
    from django.db.models import Sum
    completed_orders_list = Order.objects.filter(status='completed').select_related('product')
    total_revenue = sum(order.product.price for order in completed_orders_list) if completed_orders_list else 0
    average_order = total_revenue / completed_orders if completed_orders > 0 else 0
    success_rate = (completed_orders / total_orders * 100) if total_orders > 0 else 0
    
    # Products by type
    products_by_type = Product.objects.values('product_type').annotate(count=Count('id'))
    games_count = next((item['count'] for item in products_by_type if item['product_type'] == 'game'), 0)
    subscriptions_count = next((item['count'] for item in products_by_type if item['product_type'] == 'subscription'), 0)
    hardware_count = next((item['count'] for item in products_by_type if item['product_type'] == 'hardware'), 0)
    
    return render(request, 'dashboard/dashboard.html', {
        'total_users': total_users,
        'total_products': total_products,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
        'rejected_orders': rejected_orders,
        'games_count': games_count,
        'subscriptions_count': subscriptions_count,
        'hardware_count': hardware_count,
        'total_revenue': total_revenue,
        'average_order': average_order,
        'success_rate': success_rate,
    })

@user_passes_test(is_admin)
def dashboard_products(request):
    products = Product.objects.all()
    return render(request, 'dashboard/products.html', {'products': products})

@user_passes_test(is_admin)
def dashboard_add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            
            # جمع Features من checkboxes
            features = []
            for i in range(1, 20):
                feature = request.POST.get(f'feature_{i}')
                if feature:
                    features.append(feature)
            product.features = ', '.join(features)
            
            product.save()
            messages.success(request, 'تم إضافة المنتج بنجاح!')
            return redirect('dashboard_products')
    else:
        form = ProductForm()
    return render(request, 'dashboard/add_product.html', {'form': form})

@user_passes_test(is_admin)
def dashboard_edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            
            # جمع Features من checkboxes
            features = []
            for i in range(1, 20):
                feature = request.POST.get(f'feature_{i}')
                if feature:
                    features.append(feature)
            product.features = ', '.join(features)
            
            product.save()
            messages.success(request, 'تم تحديث المنتج بنجاح!')
            return redirect('dashboard_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/edit_product.html', {'form': form, 'product': product})

@user_passes_test(is_admin)
def dashboard_delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'تم حذف المنتج بنجاح!')
    return redirect('dashboard_products')

@user_passes_test(is_admin)
def dashboard_users(request):
    users = UserProfile.objects.select_related('user').all()
    return render(request, 'dashboard/users.html', {'users': users})

@user_passes_test(is_admin)
def dashboard_toggle_admin(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)
        # Don't allow removing admin from yourself
        if user != request.user:
            user.is_staff = not user.is_staff
            user.is_superuser = user.is_staff
            user.save()
            status = 'admin' if user.is_staff else 'user'
            messages.success(request, f'تم تغيير صلاحيات {user.username} إلى {status}')
    return redirect('dashboard_users')

@user_passes_test(is_admin)
def dashboard_change_password(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            
            # إرسال الإيميل
            if user.email:
                try:
                    send_mail(
                        'تم تغيير كلمة المرور - Angry Store',
                        f'مرحباً {user.username},\n\nتم تغيير كلمة المرور الخاصة بك بنجاح.\n\nكلمة المرور الجديدة: {new_password}\n\nيرجى تسجيل الدخول باستخدام كلمة المرور الجديدة.\n\nشكراً لك،\nفريق Angry Store',
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email],
                        fail_silently=False,
                    )
                    messages.success(request, f'تم تغيير كلمة المرور وإرسالها إلى {user.email}')
                except:
                    messages.warning(request, f'تم تغيير كلمة المرور لكن فشل إرسال الإيميل. كلمة المرور الجديدة: {new_password}')
            else:
                messages.warning(request, f'تم تغيير كلمة المرور. كلمة المرور الجديدة: {new_password} (المستخدم ليس لديه إيميل)')
            
            return redirect('dashboard_users')
    else:
        form = ChangePasswordForm()
    
    return render(request, 'dashboard/change_password.html', {'form': form, 'target_user': user})

@user_passes_test(is_admin)
def dashboard_orders(request):
    orders = Order.objects.select_related('user', 'product').all().order_by('-created_at')
    
    # حساب عدد الطلبات حسب الحالة
    pending_count = orders.filter(status='pending').count()
    received_count = orders.filter(status='received').count()
    processing_count = orders.filter(status='processing').count()
    completed_count = orders.filter(status='completed').count()
    rejected_count = orders.filter(status='rejected').count()
    
    return render(request, 'dashboard/orders.html', {
        'orders': orders,
        'pending_count': pending_count,
        'received_count': received_count,
        'processing_count': processing_count,
        'completed_count': completed_count,
        'rejected_count': rejected_count,
    })

@user_passes_test(is_admin)
def dashboard_update_order_status(request, pk):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=pk)
        status = request.POST.get('status')
        if status in ['pending', 'received', 'processing', 'completed', 'rejected']:
            order.status = status
            order.save()
            messages.success(request, 'تم تحديث حالة الطلب!')
    return redirect('dashboard_orders')

@login_required
def profile(request):
    total_orders = Order.objects.filter(user=request.user).count()
    completed_orders = Order.objects.filter(user=request.user, status='completed').count()
    pending_orders = Order.objects.filter(user=request.user, status='pending').count()
    recent_orders = Order.objects.filter(user=request.user).select_related('product').order_by('-created_at')[:5]
    
    return render(request, 'profile.html', {
        'total_orders': total_orders,
        'completed_orders': completed_orders,
        'pending_orders': pending_orders,
        'recent_orders': recent_orders,
    })

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).select_related('product').order_by('-created_at')
    
    status_filter = request.GET.get('status')
    if status_filter and status_filter != 'all':
        orders = orders.filter(status=status_filter)
    
    return render(request, 'my_orders.html', {'orders': orders})

@login_required
def toggle_wishlist(request, product_id):
    from .models import Wishlist
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()
    
    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, 'تم إزالة المنتج من المفضلة')
    else:
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, 'تم إضافة المنتج للمفضلة')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def wishlist_view(request):
    from .models import Wishlist
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_cart(request, product_id):
    from .models import Cart
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, 'تم زيادة الكمية')
    else:
        messages.success(request, 'تم إضافة المنتج للسلة')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def cart_view(request):
    from .models import Cart
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    total = sum(item.get_total_price() for item in cart_items)
    cart_count = cart_items.count()
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total, 'cart_count': cart_count})

@login_required
def checkout_cart(request):
    from .models import Cart
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    total = sum(item.get_total_price() for item in cart_items)
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        discord_username = request.POST.get('discord_username')
        whatsapp = request.POST.get('whatsapp')
        payment_proof = request.FILES.get('payment_proof')
        
        if payment_method and discord_username and whatsapp and payment_proof:
            # إنشاء طلب لكل منتج
            for item in cart_items:
                for _ in range(item.quantity):
                    Order.objects.create(
                        user=request.user,
                        product=item.product,
                        payment_method=payment_method,
                        discord_username=discord_username,
                        whatsapp=whatsapp,
                        payment_proof=payment_proof
                    )
            # حذف السلة
            cart_items.delete()
            messages.success(request, 'تم إرسال طلباتك بنجاح!')
            return redirect('my_orders')
    
    payment_numbers = {
        'vodafone': '01007875534',
        'instapay': '01222755348',
        'binance': 'angrystore@binance.com'
    }
    
    return render(request, 'checkout_cart.html', {
        'cart_items': cart_items,
        'total': total,
        'payment_numbers': payment_numbers
    })

@login_required
def remove_from_cart(request, cart_id):
    from .models import Cart
    cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'تم إزالة المنتج من السلة')
    return redirect('cart')

@login_required
def update_cart_quantity(request, cart_id):
    from .models import Cart
    cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
    action = request.POST.get('action')
    
    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, 'تم زيادة الكمية')
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, 'تم تقليل الكمية')
        else:
            cart_item.delete()
            messages.success(request, 'تم إزالة المنتج من السلة')
    
    return redirect('cart')

@user_passes_test(is_admin)
def dashboard_testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'dashboard/testimonials.html', {'testimonials': testimonials})

@user_passes_test(is_admin)
def dashboard_add_testimonial(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        text = request.POST.get('text')
        time_ago = request.POST.get('time_ago', 'منذ يومين')
        avatar_color = request.POST.get('avatar_color', 'linear-gradient(135deg, #5865F2, #7289DA)')
        
        Testimonial.objects.create(
            username=username,
            text=text,
            time_ago=time_ago,
            avatar_color=avatar_color
        )
        messages.success(request, 'تم إضافة الرأي بنجاح!')
        return redirect('dashboard_testimonials')
    return render(request, 'dashboard/add_testimonial.html')

@user_passes_test(is_admin)
def dashboard_delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.delete()
    messages.success(request, 'تم حذف الرأي بنجاح!')
    return redirect('dashboard_testimonials')

def nitro_page(request):
    products = Product.objects.filter(is_active=True, category='nitro')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'nitro.html', {'products': products})

def software_page(request):
    products = Product.objects.filter(is_active=True, category='software')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'software.html', {'products': products})

def streaming_page(request):
    products = Product.objects.filter(is_active=True, category='streaming')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'streaming.html', {'products': products})

def pc_parts_page(request):
    products = Product.objects.filter(is_active=True, category='pc_parts')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'pc_parts.html', {'products': products})

def accessories_page(request):
    products = Product.objects.filter(is_active=True, category='accessories')
    search = request.GET.get('search')
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request, 'accessories.html', {'products': products})
