from words import word_list
import random

def get_word():
    word = random.choice(word_list)
    print(word)
    return word

get_word()