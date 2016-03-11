from django.test import TestCase
from app.models import Customer, Category
# Create your tests here.

class CustomerTest(TestCase):
    """
    Class for Customer model test
    """

    def setUp(self):
        Customer.objects.create(first_name='Jhon', last_name='Doe', email='jdoe@testapp.com',
            phone_number='+580394866', address='Las Vegas' )
        Customer.objects.create(first_name='Bran', last_name='Stark', email='bstark@westeros.com',
            address='Winterfell')

    def test_customer_creation(self):
        customer1 = Customer.objects.get(first_name='Jhon', last_name='Doe')
        customer2 = Customer.objects.get(last_name='Stark', email='bstark@westeros.com')
        self.assertEqual(customer1.email, 'jdoe@testapp.com')
        self.assertEqual(customer2.first_name, 'Bran')
        self.assertEqual(customer2.address, 'Winterfell')


class CategoryTest(TestCase):
    """
    Class for Category model test
    """

    def setUp(self):
        Category.objects.create(name='Hogwarts', description='School of Witchcraft and Wizardry',
            slug='School-Hogwarts')
        Category.objects.create(name='KingKiller', description='KingKiller Chronicle',
            slug='Saga-KingKiller')

    def test_category_creation(self):
        category1 = Category.objects.get(slug='School-Hogwarts')
        category2 = Category.objects.get(name='KingKiller')
        self.assertEqual(category1.description, 'School of Witchcraft and Wizardry')
        self.assertEqual(category2.name, 'KingKiller')