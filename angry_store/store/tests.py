from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Order, UserProfile

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Test Game",
            description="Test Description",
            price=100.00,
            product_type="game"
        )

    def test_product_creation(self):
        game = Product.objects.get(name="Test Game")
        self.assertEqual(game.price, 100.00)
        self.assertEqual(game.product_type, "game")
