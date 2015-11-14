from django.test import TestCase, Client
from product.views import CategoryAllPage 

class RegistrPageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_page_load(self):
        response = self.client.get('/products/registr/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'templates/register.html')

    def test_register_page_registr(self):
        response = self.client.post('/products/registr/', {'username': 'testuser123456', 'password1': 'testpass', 'password2':'testpass'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/products/login/', response.items()[2][1])

    def test_register_page_registr_without_same_pass(self):
        response = self.client.post('/products/registr/', {'username': 'testuser1234567', 'password1': 'testpass', 'password2':'testpass1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The two password fields didn')

    def test_register_page_registr_without_correct_nickname(self):
        response = self.client.post('/products/registr/', {'username': 'testuser$234567', 'password1': 'testpass', 'password2':'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter a valid username')


class LoginPageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_page_load(self):
        response = self.client.get('/products/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'templates/login.html')

    def test_login_page_login(self):
        response = self.client.post('/products/login/', {'username': 'testuser123456', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)


    def test_Products24h_page_load_after_login(self):
        response = self.client.get('/products/products24h')
        self.assertEqual(response.status_code, 301)

#    def test_Products24h_page_load_content(self):
#        response = self.client.get('/products/products24h')
#        self.assertEqual(response.status_code, 200)

class HomePageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page_load(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Products app')

