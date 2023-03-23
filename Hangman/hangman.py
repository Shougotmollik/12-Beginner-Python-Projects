import random
from words import words
import string


def get_valid_word(words):
    word =random.choice(words) #randomly chooses something from the list
    while '_' in word or ' ' in word:
        word=random.choice(words)
    return word

def hangman():
    word=get_valid_word(words)
    word_letters=set(word) #letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #with the user has guessed 
    lives=6

    #taking user input letter 
    #gets here when len(word_letters)==0 OR when lives ==0
    while len(word_letters)>0 and lives>0:
        #letter used for the input 
        # " ".join (['a','b','c']) ==> "a b cd"
        
        print(f"you have {lives} lives left. ('_')","You have used these letters : ","".join(used_letters))

        #what current word is (W R D)
        word_list=[letter if letter in used_letters else '_'for letter in word]
        print("current word : "," ".join(word_list))

        user_letter=input("Type a letter whice in your mind at this momment: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1 #substructthe lives from 6 
                print("Letter not in word.")

        elif user_letter in used_letters:
            print("You already used this letter before ('_')")
        else:
            print("Invalid character!!! please try again ...")

    if lives==0:
        print(f"you died !!. The word was{word}")
    else:
        print(f"you guessed the word {word} !!")



hangman()