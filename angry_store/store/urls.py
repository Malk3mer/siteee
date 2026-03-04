from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_page, name='games_page'),
    path('games/offline/', views.offline_games, name='offline_games'),
    path('games/online/', views.online_games, name='online_games'),
    path('games/activate/', views.activate_games, name='activate_games'),
    path('subscriptions/', views.subscriptions_page, name='subscriptions_page'),
    path('subscriptions/nitro/', views.nitro_page, name='nitro_page'),
    path('subscriptions/software/', views.software_page, name='software_page'),
    path('subscriptions/streaming/', views.streaming_page, name='streaming_page'),
    path('hardware/', views.hardware_page, name='hardware_page'),
    path('hardware/pc-parts/', views.pc_parts_page, name='pc_parts_page'),
    path('hardware/accessories/', views.accessories_page, name='accessories_page'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order/<int:product_id>/', views.create_order, name='create_order'),
    
    # Cart & Wishlist
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:cart_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('order/', views.checkout_cart, name='checkout_cart'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    
    # Profile
    path('profile/', views.profile, name='profile'),
    path('my-orders/', views.my_orders, name='my_orders'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/products/', views.dashboard_products, name='dashboard_products'),
    path('dashboard/products/add/', views.dashboard_add_product, name='dashboard_add_product'),
    path('dashboard/products/edit/<int:pk>/', views.dashboard_edit_product, name='dashboard_edit_product'),
    path('dashboard/products/delete/<int:pk>/', views.dashboard_delete_product, name='dashboard_delete_product'),
    path('dashboard/users/', views.dashboard_users, name='dashboard_users'),
    path('dashboard/users/toggle-admin/<int:user_id>/', views.dashboard_toggle_admin, name='dashboard_toggle_admin'),
    path('dashboard/users/change-password/<int:user_id>/', views.dashboard_change_password, name='dashboard_change_password'),
    path('dashboard/orders/', views.dashboard_orders, name='dashboard_orders'),
    path('dashboard/orders/update/<int:pk>/', views.dashboard_update_order_status, name='dashboard_update_order_status'),
    
    # Testimonials
    path('dashboard/testimonials/', views.dashboard_testimonials, name='dashboard_testimonials'),
    path('dashboard/testimonials/add/', views.dashboard_add_testimonial, name='dashboard_add_testimonial'),
    path('dashboard/testimonials/delete/<int:pk>/', views.dashboard_delete_testimonial, name='dashboard_delete_testimonial'),
]
