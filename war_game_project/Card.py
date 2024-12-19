class Card:
    """this method gets parameters and resets them"""

    def __init__(self, value_card, suit_card):
        if type(value_card) != int:
            raise ValueError("card should be an int")
        if type(suit_card) != int:
            raise ValueError("suit should be an int")
        self.value_card = value_card
        self.suit_card = suit_card


    """this method gets a card and returns a text """

    def __str__(self):
        return f'{self.value_card} of {self.suit_card}'

    """this method takes two cards and comparing them, and returns the bigger one"""
    def __gt__(self, other):
        if self.value_card == other.value_card:
            return self.suit_card > other.suit_card
        return self.value_card > other.value_card

    """this method takes two cards and equals them"""
    def __eq__(self, other):
      if type(other) != Card:
        raise TypeError("other should be Card type")

      return self.value_card == other.value_card and self.suit_card == other.suit_card
