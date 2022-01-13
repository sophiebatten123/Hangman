"""
Import from other files
"""
import random
from rich.console import Console
from words import word_list
from hangman import hangman_list

CONSOLE = Console()
GUESSES = []


class GenerateWord:
    """
    Class to generate the random word
    """
    def __init__(self, word):
        """
        Defines the properties of the function
        """
        self.word = word

    def get_word(self):
        """
        This function generates a random word from the list
        it then returns the variable once it has been ran
        """
        word = random.choice(word_list)
        return word


def make_board(word):
    """
    Create a board consisting of empty lines the length
    of the randomly generated word. Play game is then
    initialised.
    """
    word_grid = "_" * len(word)
    letters = list(word)
    grid = list(word_grid)
    lives = 7
    hangman = 0

    print(letters)
    print(grid)

    play_game(letters, grid, lives, hangman, word)

    return grid


def play_game(letters, grid, lives, hangman, word):
    """
    User input is required for the game to begin and conditions
    have been set to specify that the input must be a letter.
    Guessed answers are then added to a list.
    """
    if letters == grid:
        CONSOLE.print(f"\nWell done! The word was [red bold]{word}[/red bold]"
                      ":smiley:\n")
        return "Game Complete"
    if lives == 0:
        print("You have no lives left. Game Over!")
        return "End Game"

    while True:
        user_input = input("\nEnter a letter within the word:\n").lower()
        if user_input.isalpha():
            if len(user_input) == 1:
                if len(GUESSES) != 0:
                    if user_input in GUESSES:
                        print(f"{grid}")
                        CONSOLE.print(f"\nYou have already tried {user_input}"
                                      "!", style='yellow')
                    else:
                        check_answers(user_input, letters, grid, lives,
                                      hangman, word)
                        return user_input
                else:
                    check_answers(user_input, letters, grid, lives,
                                  hangman, word)
                    return user_input
            else:
                print(f"{grid}")
                CONSOLE.print("\nYou must only enter a single letter."
                              " Try again!\n", style='yellow')
        else:
            print(f"{grid}")
            CONSOLE.print("\nPlease use only letters, try"
                          " again\n", style='yellow')


def check_answers(user_input, letters, grid, lives, hangman, word):
    """
    User input is then passed to the check answers function.
    This specifies if the answer is correct replace the value
    within the grid. If it is incorrect or the word is incomplete
    keep playing.
    """
    GUESSES.append(user_input)
    if user_input in letters:
        for index, letter in enumerate(letters):
            if letter == user_input:
                grid[index] = user_input

        CONSOLE.print(f"\nWell done {user_input} is in"
                      " the word!", style='bold green')
        print(f"{grid}")
    else:
        CONSOLE.print(f"\nTry Again {user_input} was"
                      " not in the word!", style='red bold')
        lives -= 1
        print(hangman_list[hangman])
        hangman += 1
        CONSOLE.print(f"\nYou have {lives} guesses"
                      " remaining", style='red bold')
        print(f"{grid}")
    play_game(letters, grid, lives, hangman, word)


def main():
    """
    Main functions are defined within here and initiated from call.
    """
    random_word = GenerateWord("word").get_word()
    make_board(random_word)


CONSOLE.print("Welcome to Hangman!\n", style='bold u')
print("The aim of the game is to guess the word by entering letters.")
print("For every incorrect answer the man will slowly be hung!\n")

if __name__ == "__main__":
    main()
