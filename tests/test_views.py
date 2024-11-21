from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from reservation.models import menu

class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.menu1 = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2 = menu.objects.create(title="Pizza", price=100, inventory=100)    

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        
    def test_create_item(self):
        response = self.client.post(reverse('menu'), {'title': 'Burger', 'price': 150, 'inventory': 100})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(menu.objects.count(), 3)
        
    def test_delete_item(self):
        response = self.client.delete(reverse('menu-detail', args=[self.menu1.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(menu.objects.count(), 1)    
        
    def test_update_item(self):
        response = self.client.put(
            reverse('menu-detail', args=[self.menu1.id]), 
            {'title': 'Burger', 'price': 150, 'inventory': 100}
        )
        self.assertEqual(response.status_code, 200)
        
    def test_get_item(self):
        response = self.client.get(reverse('menu-detail', args=[self.menu1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'IceCream')    
        
    def test_get_item_not_found(self):
        response = self.client.get(reverse('menu-detail', args=[3]))
        self.assertEqual(response.status_code, 404)
        
    def test_create_item_unauthorized(self):
        self.client.credentials()
        response = self.client.post(reverse('menu'), {'title': 'Burger', 'price': 150, 'inventory': 100})
        self.assertEqual(response.status_code, 401) 
        
    def test_update_item_unauthorized(self):
        self.client.credentials()
        response = self.client.put(
            reverse('menu-detail', args=[self.menu1.id]),
            {'title': 'Burger', 'price': 150, 'inventory': 100}
        )
        self.assertEqual(response.status_code, 401)
        
    def test_delete_item_unauthorized(self):
        self.client.credentials()
        response = self.client.delete(reverse('menu-detail', args=[self.menu1.id]))
        self.assertEqual(response.status_code, 401) 
        
    def test_get_item_unauthorized(self):
        self.client.credentials()
        response = self.client.get(reverse('menu-detail', args=[self.menu1.id]))
        self.assertEqual(response.status_code, 401) 
        
    def test_create_item_invalid_data(self):
        response = self.client.post(reverse('menu'), {'title': '', 'price': 150, 'inventory': 100})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(menu.objects.count(), 2)   
        
    def test_create_item_invalid_price(self):
        response = self.client.post(reverse('menu'), {'title': 'Burger', 'price': -10, 'inventory': 100})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(menu.objects.count(), 2)
        
    def test_create_item_invalid_inventory(self):
        response = self.client.post(reverse('menu'), {'title': 'Burger', 'price': 150, 'inventory': -10})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(menu.objects.count(), 2)   
        
    def test_create_item_invalid_title(self):
        response = self.client.post(reverse('menu'), {'title': '', 'price': 150, 'inventory': 100})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(menu.objects.count(), 2)       
        
    def test_create_item_invalid_price(self):
        response = self.client.post(reverse('menu'), {'title': 'Burger', 'price': -10, 'inventory': 100})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(menu.objects.count(), 2)   
        