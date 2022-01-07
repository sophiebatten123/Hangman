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

    print(letters)
    print(grid)

    play_game(letters, grid)

    return grid


def play_game(letters, grid):
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
        user_input = input("\nPlease enter a letter you think is contained within the word:\n")
        if user_input.isalpha():
            guesses.append(user_input)
            check_answers(user_input, letters,grid)
            return user_input
        else:
            print("Please use only letters, try again")


def check_answers(user_input, letters, grid):
    """
    User input is then passed to the check answers function.
    This specifies if the answer is correct replace the value
    within the grid. If it is incorrect or the word is incomplete 
    keep playing.
    """
    if user_input in letters:
            index = letters.index(user_input)
            grid[index] = user_input
            print(f"Your letter is at position {index}")
            print(f"Well done {user_input} is in the word!")
            print(f"Your new grid looks like {grid}")
            play_game(letters, grid)
    else:
        print(f"Try Again {user_input} was not in the word!")
        play_game(letters, grid)
        

def main():
    word = get_word()
    make_board(word)

print("Welcome to Hangman!")
print("To begin playing you must first guess a letter contained within the word:\n")
main()