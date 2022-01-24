import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word :
        word = random.choice(words)
    return word.upper()

def hangman():

    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    

    while len(word_letters) > 0 :
        print('You have used these letters : ' , ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word : ', ' '.join(word_list))

        
        user_letter = input('Guess a letter : ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
    
        elif user_letter in used_letters:
            print('You have already used this . Please try again')
    
        else :
            print('Invalid Character')

    print('YAY! You guessed the word', word, '!!')

hangman()