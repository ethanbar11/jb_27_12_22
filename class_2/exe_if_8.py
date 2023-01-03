score_A = int(input('Please enter the score of team A:'))
score_B = int(input('Please enter the score of team B:'))
if score_A > score_B:
    print('A team won!')
elif score_B > score_A:
    print('B team won!')
elif score_B == score_A:
    print('There was a draw.')
