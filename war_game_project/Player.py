from random import randint

from war_game_project.DeckOfCards import DeckOfCards


class Player:

    """this method gets parameters - resets them & returns them"""
    def __init__(self, player_name, number_of_cards=26):
        if type(player_name) != str:
            raise TypeError("player name should be str")
        if not 10 <= number_of_cards <= 26:
            number_of_cards = 26
        self.player_name = player_name
        self.deck = []
        self.number_of_cards = number_of_cards

    """this method gets every time a random card for the player from the deck, and she does it randomly bc of the loop """
    def set_hand(self, deck_of_cards):
        for i in range(self.number_of_cards):
            self.deck.append(deck_of_cards.deal_one())

    """this method gets a random card from the list and shows it"""
    def get_card(self):
        if len(self.deck) > 0:
            return self.deck.pop(randint(0, len(self.deck) - 1))

    """this method adding a card to the list"""
    def add_card(self, card):
        self.deck.append(card)
