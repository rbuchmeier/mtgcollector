import unittest

import get_data
import examples


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_nicify_cards(self):
        input_cards = examples.CARDS_FROM_API
        expected_cards = [{'uri': 'https://api.scryfall.com/cards/3066cc8b-7a5a-4822-a202-dd560a4fda85', 'name': 'Snow-Covered Plains', 'usd': None, 'usd_foil': '17.24', 'tix': None, 'collector_number': '1', 'image': 'https://c1.scryfall.com/file/scryfall-cards/normal/front/3/0/3066cc8b-7a5a-4822-a202-dd560a4fda85.jpg?1582068505'}, {'uri': 'https://api.scryfall.com/cards/3d7c3929-cd56-448d-9752-6d5f9d1fd778', 'name': 'Snow-Covered Island', 'usd': None, 'usd_foil': '26.44', 'tix': None, 'collector_number': '2', 'image': 'https://c1.scryfall.com/file/scryfall-cards/normal/front/3/d/3d7c3929-cd56-448d-9752-6d5f9d1fd778.jpg?1582068511'}]
        actual_cards = get_data.nicify_cards(input_cards)
        self.assertEqual(actual_cards, expected_cards)

if __name__ == '__main__':
    unittest.main()
