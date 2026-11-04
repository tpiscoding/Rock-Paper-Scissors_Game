
Rock Paper Scissors Game

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/tpiscoding/Rock-Paper-Scissors_Game/badge)](https://scorecard.dev/viewer/?uri=github.com/tpiscoding/Rock-Paper-Scissors_Game)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/16320/badge)](https://www.bestpractices.dev/projects/16320)

-- About --

My Rock, Paper, Scissors game is a command-line Python game where the player competes against a computer that randomly selects Rock, Paper, or Scissors from a list of choices within a dictionary.

Requirements:
- Python 3

How to Installation:
1. Download or clone this repository.
2. Open the project folder.
3. Run the revised version of the game:

How to Play:
1. Enter your name when prompted
2. Select one of the following choices:
   - 1 = Rock
   - 2 = Paper
   - 3 = Scissors
3. Computer randomly selects its choice.
4. The game determines the result of the round.
5. The current score is displayed.
6. Enter `y` to play another round or `n` to quit.
----------------------------------------

Game Rules
- Rock beats Scissors.
- Paper beats Rock.
- Scissors beats Paper.
- Identical choices result in a tie.

------------------------------------------------

Input and Output

Inputs:
- Player's name: Entered through the terminal.
- Player's choice: Chosen integer (1, 2, or 3).
- Continue playing: Chosen by pressing `y` or `n` key.

**Outputs:**
- A welcome message displaying the player's name.
- The result of each round.
- The current player and computer scores.
- The final scores when the player quits.

Error Handling:

The game validates the player's choices.

If the player enters an invalid number or nonnumeric value, the program displays an error message and requests another selection.

If the player enters anything other than `y` or `n` when asked to continue, the program requests valid input.

```bash
python "rock paper scissors revised.py"
```

Source Files:

- `rock, paper, scissors.py` — Original game
- `rock paper scissors revised.py` — Revised version

Feedback and Contributions:

Bug reports and suggestions can be submitted through GitHub Issues.

*if you want to contribute, fork the repository + make your changes in a new branch, and submit a pull request explaining the changes.


* This project uses OpenSSF Scorecard to monitor repository security practices *
