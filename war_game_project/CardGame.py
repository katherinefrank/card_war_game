from war_game_project.Player import Player
from war_game_project.DeckOfCards import DeckOfCards


class CardGame:
    """this method gets parameters + making + getting one method from her, and resets them"""

    def __init__(self, player_name1, player_name2, number_of_cards=26):
        if not 10 <= number_of_cards <= 26:
            number_of_cards = 26
        if type(number_of_cards) != int:
            raise TypeError
        self.numbers_of_cards = number_of_cards
        self.player1 = Player(player_name1, number_of_cards)
        self.player2 = Player(player_name2, number_of_cards)
        self.deck = DeckOfCards()
        self.new_game()

    """this method making a new game"""

    def new_game(self):
        if len(self.deck.cards) == 52:
            self.deck.cards_shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)

    """this method returns who the winner is. if there is a tie, she returns nothing"""

    def get_winner(self):
        if len(self.player2.deck) > len(self.player1.deck):
            return self.player2
        if len(self.player1.deck) > len(self.player2.deck):
            return self.player1
        return None
