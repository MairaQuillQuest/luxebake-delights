from django.test import TestCase
from .models import Product, Order, OrderItem
from django.contrib.auth.models import User

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Croissant', description='Buttery pastry', price=3.50, stock=10)

    def test_product_name(self):
        croissant = Product.objects.get(name='Croissant')
        self.assertEqual(croissant.name, 'Croissant')

    def test_product_stock(self):
        croissant = Product.objects.get(name='Croissant')
        self.assertEqual(croissant.stock, 10)

# Add more tests for other models if needed

class OrderTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='password')
        Order.objects.create(user=user, total_price=10.50)

    def test_order_user(self):
        order = Order.objects.get(total_price=10.50)
        self.assertEqual(order.user.username, 'testuser')

    def test_order_total_price(self):
        order = Order.objects.get(total_price=10.50)
        self.assertEqual(order.total_price, 10.50)

# Add more tests for other models if needed

class OrderItemTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='password')
        order = Order.objects.create(user=user, total_price=10.50)
        product = Product.objects.create(name='Croissant', description='Buttery pastry', price=3.50, stock=10)
        OrderItem.objects.create(order=order, product=product, quantity=2)

    def test_order_item_quantity(self):
        order_item = OrderItem.objects.get(quantity=2)
        self.assertEqual(order_item.quantity, 2)

    # Add more tests for other aspects of OrderItem if needed
