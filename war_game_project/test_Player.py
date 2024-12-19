from unittest import TestCase

from war_game_project.DeckOfCards import DeckOfCards
from war_game_project.Player import Player
from war_game_project.Card import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("barel", 26)

    def test_init_valid(self):
        self.assertEqual(self.player.player_name, "barel")
        self.assertEqual(self.player.number_of_cards, 26)

    def test_init_default_range(self):
        self.player1 = Player("bob", 9)
        self.assertEqual(self.player1.number_of_cards, 26)

    def test_init_invalid(self):
        with self.assertRaises(TypeError):
            Player(3, 26)

    def test_set_hand_valid(self):
        deck = DeckOfCards()
        self.player.set_hand(deck)
        self.assertEqual(26, len(self.player.deck))

    def test_get_card_valid(self):
        self.player.deck.append(Card(1, 1))
        self.assertEqual(Card(1,1),self.player.get_card())

    def test_add_card_valid(self):
        self.player.add_card(Card(1,1))
        self.assertIn(Card(1,1),self.player.deck )




