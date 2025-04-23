import random

choices_dict = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

def rps_game():
    player1_score = 0
    player2_score = 0
    player1_name = str(input("Enter your name: "))

    print(f"Welcome {player1_name} to a game of Rock, Paper, Scissors. Play if you dare!")

    while True: # input loop for valid choice
        while True:
            try:
                player1_choice = int(input("Pick 1 for Rock, 2 for Paper, 3 for Scissors: "))
                if player1_choice not in [1, 2, 3]:
                    raise ValueError("Number is not in range of choices. Pick 1 for Rock, 2 for Paper, 3 for Scissors.")
                break  # valid input, exit input loop
            except ValueError as ve:
                print(ve)

        # main game loop

        player2_choice = random.choice(list(choices_dict.values()))

        if player1_choice == player2_choice: # if you tie
            print(f"You've tied with Player 2! "
                  f"\nThe current score is: \nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

        elif player1_choice == 1 and player2_choice == 3: # rock vs scissors
            player1_score += 1
            print(f"Rock crushes scissors! \nThe current score is:"
                  f"\nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

        elif player1_choice == 2 and player2_choice == 1: # paper vs rock
            player1_score += 1
            print(f"Paper covers rock! \nThe current score is:"
                  f"\nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

        elif player1_choice == 3 and player2_choice == 2: # scissors vs paper
            player1_score += 1
            print(f"Scissors cuts paper! \nThe current score is:"
                  f"\nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

        else: # if you lose
            player2_score += 1
            print(f"You lose! \nThe current score is:"
                  f"\nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

        # player choice to stop
        while True:
            try:
                user_input = input("Do you want to continue playing? y/n: ").lower()
                if user_input not in ['y', 'n']:
                    raise ValueError("Invalid input. Please enter 'y' to continue or 'n' to stop.")
                if user_input == 'n':
                    print(f"The final score is: \nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")
                    return
                else:
                    break
            except ValueError as p:
                print(p)

rps_game()