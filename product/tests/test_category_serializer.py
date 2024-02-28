# type: ignore
from django.test import TestCase
from product.factories import CategoryFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="technology")
        self.category_serializer = CategorySerializer(self.category)

    def test_order_serializer(self):
        serializer_data = self.category_serializer.data
        self.assertEqual(serializer_data["title"], "technology")
