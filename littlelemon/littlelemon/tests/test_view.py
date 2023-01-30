from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


# Create your tests here.
class MenuViewSetTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="TestMenuItem", price=80, inventory=100)
    
    def test_get_all(self):
        items =  Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        self.assertEqual(len(serialized_items.data), 1)
