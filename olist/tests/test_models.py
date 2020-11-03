from django.test import TestCase
from olist.models import Category
from olist.models import Product


class ModelsTestCase(TestCase):


    @classmethod
    def setUpTestData(cls):
        ret_category = Category.objects.create(name="Bebida")       # pylint: disable=no-member
        product = Product.objects.create(name="Refrigerante",description="Refrigerante de 2L",value="10")     # pylint: disable=no-member
        product.category.add(ret_category)

    def test_category_name_label(self):
        category = Category.objects.get(pk=1)       # pylint: disable=no-member
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_name_max_length(self):
        category = Category.objects.get(pk=1)       # pylint: disable=no-member
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)
    
    def test_product_get(self):
        product = Product.objects.get(pk=1)       # pylint: disable=no-member
        self.assertEquals(product.name, 'Refrigerante')

    def test_product_name_max_length(self):
        product = Product.objects.get(pk=1)       # pylint: disable=no-member 
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)   

    def test_product_description_max_length(self):
        product = Product.objects.get(pk=1)       # pylint: disable=no-member 
        max_length = product._meta.get_field('description').max_length
        self.assertEquals(max_length, 100)     
        


 
