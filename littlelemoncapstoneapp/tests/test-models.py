from django.test import TestCase
from littlelemoncapstoneapp.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title = "Ice Cream", price = 8.80, quantity = 4)
        self.assertEqual(str(item), "Ice Cream")