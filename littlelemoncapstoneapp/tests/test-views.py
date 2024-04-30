from django.test import TestCase
from littlelemoncapstoneapp.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Water", price=5, quantity=3)
        Menu.objects.create(title="Water2", price=5.1, quantity=3)
        Menu.objects.create(title="Water3", price=5.2, quantity=3)