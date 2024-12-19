from war_game_project.CardGame import CardGame

name = input("enter name: ")
name2 = input("enter second name: ")
num_of_cards = 26
print(
    f'the name is {name}, and the number of cards is {num_of_cards} "the second name is {name2}, "and the number of cards is {num_of_cards} ')

card_game = CardGame(name, name2, num_of_cards)

# Main game loop
for i in range(10):
    card1 = card_game.player1.get_card()
    card2 = card_game.player2.get_card()

    # Ensure that both cards are valid (not None)
    if card1 is None or card2 is None:
        print(f"One of the players has no more cards! Ending the game.")
        break  # Exit the loop if either player runs out of cards

    print(f'{card_game.player1.player_name} put the card: {card1.value_card} of suit {card1.suit_card}')
    print(f'{card_game.player2.player_name} put the card: {card2.value_card} of suit {card2.suit_card}')

    if card1 > card2:
        print(f'{card_game.player1.player_name} won this round! \n')
        card_game.player1.add_card(card1)
        card_game.player1.add_card(card2)

    elif card2 > card1:
        print(f'{card_game.player2.player_name} won this round! \n')
        card_game.player2.add_card(card1)
        card_game.player2.add_card(card2)

print(f'Congrats! The game is over! Did you have fun?')
winner = card_game.get_winner()

if winner:
    print(f'The winner is {winner.player_name} with {len(winner.deck)} cards left.')
else:
    print("It's a TIE! Both players are winners!")
