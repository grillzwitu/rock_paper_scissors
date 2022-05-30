import random

def start_game():

    plays = ["R", "P", "S"]

    user_play = input('Please choose a play, please enter, R, P, S: ').upper()

    while user_play:
        if user_play in plays:
            break
        else:
            print('Please enter a valid play option')
            user_play = input('Please choose a play, please enter, R, P, S: ').upper()

    cpu_play = random.choice(plays)

    if user_play == "R":
        user_play = "Rock"
    elif user_play == "P":
        user_play = "Paper"
    elif user_play == "S":
        user_play = "Scissors"

    if cpu_play == "R":
        cpu_play = "Rock"
    elif cpu_play == "P":
        cpu_play = "Paper"
    elif cpu_play == "S":
        cpu_play = "Scissors"

    print(f'Player ({user_play}) : CPU ({cpu_play})')

    if user_play == "Rock" and cpu_play == "Scissors":
        print('You win!!!')
    elif user_play == "Scissors" and cpu_play == "Rock":
        print('CPU wins!!!')
    elif user_play == "Rock" and cpu_play == "Paper":
        print('CPU wins!!!')
    elif user_play == "Paper" and cpu_play == "Rock":
        print('You win!!!')
    elif user_play == "Scissors" and cpu_play == "Paper":
        print('You win!!!')
    elif user_play == "Paper" and cpu_play == "Scissors":
        print('CPU wins!!!')
    elif user_play == cpu_play:
        print('Its a tie')
        start_game()

start_game()
