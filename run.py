from words import word_list
import random

def get_word():
    """
    This function generates a random word from the list 
    it then returns the variable once it has been ran
    """
    word = random.choice(word_list)
    print(word)
    return word

def make_board(word):
    word_grid = " ___ " * len(word)
    print(word_grid)
    return word_grid

def main():
    word = get_word()
    make_board(word)

main()