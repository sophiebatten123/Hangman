from words import word_list
import random

def get_word():
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
    lives = 3

    print(letters)
    print(grid)

    play_game(letters, grid, lives)

    return grid


def play_game(letters, grid, lives):
    """
    User input is required for the game to begin and conditions
    have been set to specify that the input must be a letter.
    Guessed answers are then added to a list.
    """
    guesses = []
    if letters == grid:
        print(f"Well done you have completed the game the word was {letters}\n")
        return (f"Well done you have completed the game the word was {letters}")
    while True:
        user_input = input("\nEnter a letter you think is within the word:\n")
        if user_input.isalpha():
            guesses.append(user_input)
            check_answers(user_input, letters, grid, lives)
            return user_input
        else:
            print("Please use only letters, try again")


def check_answers(user_input, letters, grid, lives):
    """
    User input is then passed to the check answers function.
    This specifies if the answer is correct replace the value
    within the grid. If it is incorrect or the word is incomplete 
    keep playing.
    """
    if user_input in letters:
        print(letters)
        index = letters.index(user_input)
        grid[index] = user_input
        print(f"{index}")
        print(f"Well done {user_input} is in the word!")
        print(f"{grid}")
        play_game(letters, grid, lives)
    else:
        print(f"Try Again {user_input} was not in the word!")
        lives -= 1
        print(f"You have {lives} remaining")
        play_game(letters, grid, lives)
        

def main():
    word = get_word()
    make_board(word)

print("Welcome to Hangman!")
print("To begin playing you must first guess a letter contained within the word:\n")
main()