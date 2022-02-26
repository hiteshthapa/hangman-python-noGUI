# Coding Challenge 3, hangman.py
# Hangman Game


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")    
    file = open(WORDLIST_FILENAME, 'r')    
    line = file.readline()    
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(word, letters_guessed):
    count = 0
    for letters in word:
        if letters in letters_guessed:
            count += 1
    if count == len(word):
        return True
    else:
        return False


def get_guessed_word(word, letters_guessed):
    temp = []
    string1 = ""
    for key in word:
        if key in letters_guessed:
            string1 += key
        else:
            string1 += "_ "
    return string1


def get_available_letters(letters_guessed):
    import string
    count = 0
    s = string.ascii_lowercase

    string1 = ""
    for letter in s:
        if letter in letters_guessed:
            count += 1
        else:
            string1 += letter
    return string1


def hangman(word):
    length = len(word)
    print("Welcome to Hangman game Ultimate Edition\n--------------------------------------------------------\n")
    print("I am thinking of a word that is", length, "letters long.")
    chances = 2 * len(word)
    i = 0
    letters_guessed = []
    while (chances != 0):
        print("\n--------------------------------------------------------")
        if word != get_guessed_word(word, letters_guessed):
            print("You have", chances, "guesses left.")
            print("Available letters: ", get_available_letters(letters_guessed))
            guess = input("Please guess a letter: ")
            guess_lower_case = guess.lower()

            if guess_lower_case in letters_guessed:
                print("Oops! You have guessed that letter already: ", get_guessed_word(word, letters_guessed))

            elif guess_lower_case not in word:
                print("Oops! Looks like that letter is not in my word:", get_guessed_word(word, letters_guessed))
                chances -= 1
            else:
                letters_guessed.append(guess_lower_case)
                print("Good guess: ", get_guessed_word(word, letters_guessed))                
            letters_guessed.append(guess_lower_case)
        elif word == get_guessed_word(word, letters_guessed):
            print("Congratulations, you won the game!")
            break
    else:
        print("=========================================\n")
        print("Sorry, you ran out of guesses. The word was " + word + ".\n")
    print("Thank you for playing. Your total score is:", len(word) * chances)


word = choose_word(wordlist)



word = choose_word(wordlist).lower()
hangman(word)
