"""
This is a Hangman Game made by AP. The goal is to have a randomly chosen word picked at the start of the program.
You get to choose letters of the alphabet to spell out the word.
5 wrong guesses then you're done!
"""
from english_words import english_words_lower_alpha_set
import random


def wordPick() -> list:
    """Picks a random word from a very large list of english words varied in length."""
    word = []
    engWordList = list(english_words_lower_alpha_set)
    pickedWord = random.choice(engWordList)
    word[:] = pickedWord
    return word


def playHangMan(word: list) -> str:
    """Checks guessed letters versus word"""
    correctList = []
    guessList = []
    wrongGuess = 0
    finalWord = "".join([str(item) for item in word])
    for x in range(len(word)):
        correctList.append("-")
    print(*correctList)
    while wrongGuess <= 5:
        guess = input("Guess a letter!\n-> ")
        if guess in guessList:
            print("You already have guessed that DINGUS!")
            continue
        if guess in word:
            print("CORRECT!")
            for i in range(len(word)):
                if guess == word[i]:
                    correctList[i] = word[i]
            print(*correctList)
        else:
            wrongGuess += 1
            print("INCORRECT! You have", 6 - wrongGuess, "wrong guesses left!")
            if wrongGuess == 1:
                print("\t|-----|\n"
                      "\t|   ('-')\n"
                      "\t|\n"
                      "\t|\n"
                      "\t|\n"
                      "__-----__")
            if wrongGuess == 2:
                print("\t|-----|\n"
                      "\t|   ('-')\n"
                      "\t|     |\n"
                      "\t|\n"
                      "\t|\n"
                      "__-----__")
            if wrongGuess == 3:
                print("\t|-----|\n"
                      "\t|   ('-')\n"
                      "\t|     |\ \n"
                      "\t|\n"
                      "\t|\n"
                      "__-----__")
            if wrongGuess == 4:
                print("\t|-----|\n"
                      "\t|   ('-')\n"
                      "\t|    /|\ \n"
                      "\t|\n"
                      "\t|\n"
                      "__-----__")
            if wrongGuess == 5:
                print("\t|-----|\n"
                      "\t|   ('-')\n"
                      "\t|    /|\ \n"
                      "\t|      \ \n"
                      "\t|\n"
                      "__-----__")
            if wrongGuess == 6:
                print("\t|-----|\n"
                      "\t|   (x_x)\n"
                      "\t|    /|\ \n"
                      "\t|    / \ \n"
                      "\t|\n"
                      "__-----__")
            print(*correctList)
        guessList.append(guess)
        if correctList == word:
            print("Congratulations! The word is:\t", finalWord)
            print("\n")
            return "winner"
    if wrongGuess == 6:
        print("You lost! The word was:\t", finalWord)
        print("\n")
        return "loser"
