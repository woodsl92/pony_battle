import unittest
from unittest.mock import patch
import pony_battle

class TestPony(unittest.TestCase):
    def setUp(self):
        self.pony = pony_battle.Pony("Test Pony", magic=5, kindness=5, laughter=5, generosity=5, loyalty=5, honesty=5)

    def test_initialization(self):
        self.assertEqual(self.pony.name, "Test Pony")
        self.assertEqual(self.pony.stats['magic'], 5)
        self.assertEqual(self.pony.stats['kindness'], 5)
        self.assertEqual(self.pony.stats['laughter'], 5)
        self.assertEqual(self.pony.stats['generosity'], 5)
        self.assertEqual(self.pony.stats['loyalty'], 5)
        self.assertEqual(self.pony.stats['honesty'], 5)

    def test_generate_random_modifier(self):
        modifiers = self.pony.generate_random_modifier()
        self.assertEqual(len(modifiers), 6)
        for modifier in modifiers.values():
            self.assertIn(modifier, range(-2, 3))

    @patch('pony_battle.Pony.generate_random_modifier', return_value={'magic': 1, 'kindness': 1, 'laughter': 1, 'generosity': 1, 'loyalty': 1, 'honesty': 1})
    def test_calculate_total_score(self, mock_generate_random_modifier):
        total_score = self.pony.calculate_total_score()
        self.assertEqual(total_score, 36)  # 6 traits * (5 base + 1 modifier)

if __name__ == '__main__':
    unittest.main()