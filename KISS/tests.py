import unittest
from solution import count_fruits


class TestCountFruits(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.eleven_fruits_data = [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]

        cls.three_fruits_data = ["banana", "cherry", "apple"]
        cls.empty_fruits_data = []

    def test_count_fruits(self):
        self.assertEqual(
            count_fruits(self.eleven_fruits_data),
            {"apple": 4, "banana": 3, "cherry": 4},
        )
        self.assertEqual(
            count_fruits(self.three_fruits_data), {"apple": 1, "banana": 1, "cherry": 1}
        )

    def test_count_empty_data(self):
        self.assertEqual(count_fruits(self.empty_fruits_data), {})
