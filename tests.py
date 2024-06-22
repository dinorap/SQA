from django.test import TestCase
from .models import Product, Order, Customer
import datetime

class TestProductModel(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Laptop',
            description='A high-performance laptop',
            price=999.99,
            stock=10,
            sku='LAP12345'
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Laptop')

    def test_product_price_with_discount(self):
        discount = Discount.objects.create(
            product=self.product,
            discount_percentage=10,
            valid_from=datetime.date.today(),
            valid_to=datetime.date.today() + datetime.timedelta(days=10)
        )
        self.assertEqual(self.product.price_with_discount(), 899.99)

class TestOrderModel(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone_number='+1234567890',
            address='123 Main St., Anytown, USA'
        )
        self.product = Product.objects.create(
            name='Laptop',
            description='A high-performance laptop',
            price=999.99,
            stock=10,
            sku='LAP12345'
        )
        self.order = Order.objects.create(
            customer=self.customer,
            status='Pending',
            order_date=datetime.date.today()
        )
        self.order.items.create(
            product=self.product,
            quantity=1,
            price=self.product.price
        )

    def test_order_total_price(self):
        self.assertEqual(self.order.total_price(), 999.99)
