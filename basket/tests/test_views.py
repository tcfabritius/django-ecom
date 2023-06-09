from django.contrig.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Product, Category


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django advanced', created_by_id=1,
                               slug='django-advanced', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django intermediate', created_by_id=1, 
                               slug='django-intermediate', price='20.00', image='django')
        self.client.post(reverse('basket:basket_add'), {'productid': 1, 'productqty': 1, 'action': 'post'})
        self.client.post(reverse('basket:basket_add'), {'productid': 2, 'productqty': 2, 'action': 'post'})

    def test_basket_url(self):
        """
        Test basket url
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test basket add
        """
        response = self.client.post(reverse('basket:basket_add'), {'productid': 1, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json().get('qty'), 4)
        response = self.client.post(reverse('basket:basket_add'), {'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json().get('qty'), 3)

    def test_basket_delete(self):
        """
        Test basket delete
        """
        response = self.client.post(reverse('basket:basket_delete'), {'productid': 2, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '20.00'})

    def test_basket_update(self):
        """
        Test basket update
        """
        response = self.client.post(reverse('basket:basket_update'), {'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})