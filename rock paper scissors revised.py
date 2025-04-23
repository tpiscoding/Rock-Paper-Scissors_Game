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


    print(f"Welcome {player1_name} to our game of Rock, Paper, Scissors.")

    while True:
        try:
            player1_choice = int(input("Pick 1 for Rock, 2 for Paper, 3 for Scissors: "))
            player2_choice = random.choice(list(choices_dict.values()))

            if player1_choice == player2_choice:  # tie
                print(f"You've tied with Player 2! "
                      f"\nThe current score is: \nPlayer 1: {player1_score} \nPlayer 2: {player2_score} " )

            elif player1_choice == 1 and player2_choice == 3:  # rock vs scissors
                player1_score += 1
                print(f"Rock crushes scissors! \nThe current score is: "
                      f"\nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

            elif player1_choice == 2 and player2_choice == 1:  # paper vs rock
                player1_score += 1
                print(f"Paper covers rock! \nThe current score is: "
                      f"\nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

            elif player1_choice == 3 and player2_choice == 2:  # scissors vs paper
                player1_score += 1
                print(f"Scissors cuts paper! \nThe current score is: "
                      f"\nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

            else: # if you lose
                player2_score += 1
                print(f"You lose! \nThe current score is: "
                      f"\nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")

        except ValueError: # exception if you input an answer that's not 1, 2, or 3
            print("That's an invalid choice. Try again.")
        while True:
            try:
                user_input = input("Do you want to stop playing? y/n: ").lower()
                if user_input not in ['y', 'n']:
                    raise ValueError("Invalid input. Please enter 'y' to end or 'n' to continue.")
                if user_input == 'y':
                    print(f"The final score is: \nPlayer 1: {player1_score} \nPlayer 2: {player2_score}")
                    return  # exits the game
                else:
                    break  # continue the game loop
            except ValueError as p:
                print(p)

rps_game()