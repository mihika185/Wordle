import random

MAX_TRIES = 6

BRED = '\033[1;31m'
BGRN = '\033[1;32m'
BYEL = '\033[1;33m'
RESETC = '\033[0m'

words  =["APPLE", "BASES", "PLAYS", "STRAW", "LEMON", "SLUMS"]

def match(secret, guess):
    result = [''] * 5
    #print(result)
    copy_secret = secret[:]
    for i, letter in enumerate(guess): # enumerate gives index of letter in a word
        if letter == copy_secret[i]:
            copy_secret = copy_secret[:i] + ' ' + copy_secret[i+1:]
            result[i] = 'G'
    
    #print(result[4])
    for i, letter in enumerate(guess):
        #print(i)
        if result[i] == '':
            loc = copy_secret.find(letter) #.find() gives the index of first occurrenve of that letter
                                           # if the letter isn't there then it'll give -1
            if loc>=0:
                copy_secret = copy_secret[:i] + ' ' + copy_secret[i+1:]
                result[i] = 'Y'
            else:
                result[i] = 'R'

    return result

def main():
    while True:
        secret = random.choice(words)
        print("Welcome to Wordle!")
        print("Guess the 5 letter word.")
        
        tries = 0
        while tries<MAX_TRIES:
            input_word = input("> ").strip().upper() # Function Chaining
            if (len(input_word) != 5):
                    print("Please enter a 5-letter word.")
                    continue

            result = match(secret, input_word)

            print("Result: ", end = "") #By defalut '\n' is the end in python

            for i in range(5):
                if(result[i] == 'G'):
                    print(BGRN, end="")
                
                elif result[i] == 'Y':
                    print(BYEL, end="")

                elif result[i] == 'R':
                    print(BRED, end="")

                print(input_word[i], end = "")
                print(RESETC, end = "")
            print()

            if secret == input_word:
                print("Congratulations! You guessed the word.")
                break
            tries += 1

        if tries == MAX_TRIES:
            print("Sorry you ran out of guesses. The word was: ", secret)
main()