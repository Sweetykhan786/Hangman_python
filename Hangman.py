from words import choose_word
from images import IMAGES
def valid(input):
    if len(input)!=1:
        return False
    if not input.isalpha():
        return False
    return True
def is_word_guessed(secret_word,letters_guessed):
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True
    return False
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    letters_left=""
    for i in letters_guessed:
        if i not in letters_guessed:
            letters_left+=i
            # letters_left=letters_left.replace(i,"")
        return letters_left
    # letters_left = ""
def get_hint(secret_word, letters_guessed):
    import random
    letters_not_guessed=[]
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letters_not_guessed:
                letters_not_guessed.append(i)
        i+=1
    return random.choice(letters_not_guessed)
# remaining_lives=8
def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print(str(len(secret_word)),"secret_wordsecretword_word")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = []
    # level=input("enter the level in which you want to play:\n(a)Easy\n(b)Medium")
    total_lives=remaining_lives=8
    images_select_last_indices=[0,1,2,3,4,5,6,7]
    level=input("Enter the level in which you want to play:\n(a)Easy    \n(b)Medium   ")
    if level=="b":
        total_lives=remaining_lives=6
        image_selection=[0,1,2,3,4,5,6]
    elif level=="a":
        total_lives=remaining_lives=8
        image_selection=[0,1,2,3,4,5,6,7]
    else:
        if level!="a":
            print("invalid choice")

    # remaining_lives=8
    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        # print ("Available letters: " + available_letters)
        guess = input("Please guess a letter: ")
        letter = guess.lower()                                                  
        if letter=="hint":
            print("hint for secret word"+get_hint(secret_word,letters_guessed))
            letter=get_hint(secret_word,letters_guessed)
            # letters_guessed.append(letter)
            # print("your hint for this secret word is".get_hint(secret_word,letters_guessed))
            # print("")
        else:
            if (not valid(letter) and letter!="hint"):
                print("invalid Output")
                continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print("good guess   "+get_guessed_word(secret_word,letters_guessed))
            print("")
            if is_word_guessed(secret_word,letters_guessed)==True:
                print("**CONGRATULATIONS YOU WON**")
                print("")
                break
        else:
            print("Oops! that letter is not in my word"+(get_guessed_word(secret_word,letters_guessed)))
            letters_guessed.append(letter)
            print(IMAGES[image_selection[total_lives-remaining_lives]])
            remaining_lives-=1
            print("remaining lives"+str(remaining_lives))
            print("")
    else:      
        print ("Sorry, you loose the game,The word was " + str(secret_word) + ".")           
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
    
    
        
    