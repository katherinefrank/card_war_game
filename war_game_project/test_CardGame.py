from unittest import TestCase
from war_game_project.CardGame import CardGame
from war_game_project.DeckOfCards import DeckOfCards
from war_game_project.Player import Player

class TestCardGame(TestCase):
    def setUp(self):
        self.card_game = CardGame("barel", "denis", 20)

    def test_init_valid(self):
        self.assertEqual("barel", self.card_game.player1.player_name)
        self.assertEqual("denis", self.card_game.player2.player_name)
        self.assertEqual(20, len(self.card_game.player1.deck))
        self.assertEqual(20, len(self.card_game.player2.deck))


    def test_init_invalid_name_type(self):
        with self.assertRaises(TypeError):
            CardGame(123, "barel", 20)
        with self.assertRaises(TypeError):
            CardGame("barel", 123, 20)

    def test_init_invalid_number_of_cards(self):
        with self.assertRaises(TypeError):
            CardGame("denis", "barel", "20")

    def test_init_invalid_hand_size_low(self):
        card_game = CardGame("denis", "barel", 9)
        self.assertEqual(26, len(card_game.player1.deck))


    def test_new_game_invalid(self):
        card_game = CardGame("barel", "denis", 5)
        playerr1 = card_game.player1
        playerr2 = card_game.player2
        deckk = card_game.deck
        card_game.new_game()
        self.assertEqual(playerr1.deck, card_game.player1.deck)
        self.assertEqual(playerr2.deck, card_game.player2.deck)
        self.assertEqual(deckk, card_game.deck)

    def test_get_winner_valid(self):
        self.card_game.player1.get_card()
        self.assertEqual(self.card_game.player2, self.card_game.get_winner())





