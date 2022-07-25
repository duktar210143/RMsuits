from django.test import TestCase, testcases
from product.models import Product

class TestProductModel(TestCase):
    def test_model_str(self):
        suit_name = Product.objects.create(suit_name = "linen")
        # content = Product.objects.create(content = "this suit is red")
        self.assertEqual(str(suit_name),"linen")
    
