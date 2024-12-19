from unittest import TestCase

from war_game_project.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_init_valid_52_cards(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_cards_shuffle_valid(self):
        og_deck = self.deck.cards.copy()
        self.deck.cards_shuffle()
        shuffle_deck = self.deck.cards
        self.assertNotEqual(og_deck, shuffle_deck)

    def test_deal_one_valid(self):
        self.deck.deal_one()
        self.assertEqual(len(self.deck.cards),51)









