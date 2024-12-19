from war_game_project.Card import Card
from random import randint
from random import shuffle

class DeckOfCards:


    """this method takes 2 parameters and blending them while adding cards to the cards list """
    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
            for value in range(1, 14):
                self.cards.append(Card(value, suit))


    """this method shuffles the list of cards"""
    def cards_shuffle(self):
        shuffle(self.cards)

    """this method checks if there is cards in the list, if there is, she pops one card from the list"""
    def deal_one(self):
        if len(self.cards) > 0:  # Ensure there is a card to deal
            return self.cards.pop(randint(0, len(self.cards) - 1))
