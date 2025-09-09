from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="BURHAN FC Jersey 2024",
            price=150000,
            description="Official match jersey of BURHAN FC season 2024",
            thumbnail="https://example.com/burhan_jersey.jpg",
            category="jerseys",
            is_featured=True
        )
        self.assertEqual(product.category, "jerseys")
        self.assertTrue(product.is_featured)
        self.assertEqual(product.name, "BURHAN FC Jersey 2024")
        
    def test_product_default_values(self):
        product = Product.objects.create(
            name="Training Football",
            price=500,
            description="High-quality training football",
            thumbnail="https://example.com/football.jpg",
            category="equipment"
        )
        self.assertEqual(product.category, "equipment")
        self.assertFalse(product.is_featured)
        self.assertFalse(product.is_premium)
        
    def test_update_price(self):
        product = Product.objects.create(
            name="Football Boots",
            price=250000,
            description="Professional football boots",
            thumbnail="https://example.com/boots.jpg",
            category="boots"
        )
        initial_price = product.price
        product.update_price(200000)  # Price drop sale
        self.assertEqual(product.price, 200000)
        self.assertNotEqual(product.price, initial_price)
        
    def test_is_premium_threshold(self):
        # Test product with exactly 1000 price (should not be premium)
        product_1000 = Product.objects.create(
            name="Standard Jersey",
            price=1000,
            description="Standard quality jersey",
            thumbnail="https://example.com/standard_jersey.jpg",
            category="jerseys"
        )
        self.assertFalse(product_1000.is_premium)
        
        # Test product with 1001 price (should be premium)
        product_1001 = Product.objects.create(
            name="Premium Jersey", 
            price=1001,
            description="Premium quality jersey with special features",
            thumbnail="https://example.com/premium_jersey.jpg",
            category="jerseys"
        )
        self.assertTrue(product_1001.is_premium)