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

class TestArgumentParsing(unittest.TestCase):
    def test_list_ponies(self):
        with patch('sys.argv', ['pony_battle.py', '--list_ponies']):
            with patch('builtins.print') as mocked_print:
                with self.assertRaises(SystemExit):
                    pony_battle.main()
                mocked_print.assert_any_call('twilight sparkle')
                mocked_print.assert_any_call('rainbow dash')
                mocked_print.assert_any_call('fluttershy')
                mocked_print.assert_any_call('applejack')
                mocked_print.assert_any_call('rarity')
                mocked_print.assert_any_call('pinkie pie')

    def test_no_arguments(self):
        with patch('sys.argv', ['pony_battle.py']):
            with self.assertRaises(SystemExit):
                with patch('argparse.ArgumentParser.print_help') as mocked_help:
                    pony_battle.main()
                    mocked_help.assert_called_once()


if __name__ == '__main__':
    unittest.main()