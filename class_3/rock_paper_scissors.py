game_is_on = True
while game_is_on == True:
    choice_1 = input('Player 1, please enter R,P,S (rock paper scissors): ')
    choice_2 = input('Player 2, please enter R,P,S (rock paper scissors): ')
    if choice_1 == choice_2:
        print('This is a tie! playing again.')
        continue
    elif choice_1 == 'R' and choice_2 == 'S':
        print('Player 1 won.')
    elif choice_1 == 'S' and choice_2 == 'R':
        print('Player 2 won.')
    elif choice_1 == 'S' and choice_2 == 'P':
        print('Player 1 won.')
    elif choice_1 == 'P' and choice_2 == 'S':
        print('Player 2 won.')
    elif choice_1 == 'P' and choice_2 == 'R':
        print('Player 1 won.')
    elif choice_1 == 'R' and choice_2 == 'P':
        print('Player 2 won.')
    else:
        print('You entered something incorrectly. You must play again.')
        continue

    should_play_again = input('If you want to play again, enter yes, else no: ')
    if should_play_again == 'no':
        game_is_on = False
