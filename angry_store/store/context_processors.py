def cart_count(request):
    if request.user.is_authenticated:
        from .models import Cart
        count = Cart.objects.filter(user=request.user).count()
        return {'cart_count': count}
    return {'cart_count': 0}
