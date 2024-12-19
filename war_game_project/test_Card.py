
from unittest import TestCase

from war_game_project.Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card=Card(6,2)
        self.card2=Card(8,1)

    def test_init_valid(self):
        self.assertEqual(self.card.value_card,6)
        self.assertEqual(self.card.suit_card,2)

    def test_init_invalid_type_of_value(self):
        with self.assertRaises(ValueError):
            Card("hi orly",2)

    def test_init_invalid_type_of_suit(self):
        with self.assertRaises(ValueError):
            Card(6,"hi again!")

    def test_gt_valid_value(self):
        self.assertTrue(self.card2 > self.card)

    def test_gt_valid_eq_suit(self):
        self.assertTrue(Card(6,2)> Card(6,1))

    def test_eq_valid(self):
        self.assertTrue(Card(9,2) == Card(9,2))


    def test_eq_invalid(self):
        with self.assertRaises(TypeError):
            self.card == "hi"












