# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

# Comment: I only count times when an actual number is given as a 'guess',
# if user given a letter or something else, then the guess giving error is not counted in 'guesses'
import random

x = random.randint(1, 9)
# print x
nroOfGuesses = 0

while True:
    guess = raw_input("Guess a number between and including numbers 1 - 9: ")
    # print guess
    if guess == 'exit':
        print 'Thank you for playing!'
        break
    else:
        try:
            guessInt = int(guess)
        except ValueError:
            print("That's not a number!")
            continue
        # print guessInt
        nroOfGuesses = nroOfGuesses + 1
        if guessInt < 1 or guessInt > 9:
            print 'Number not within range 1-9, start over'
            continue
        elif guessInt == x:
            print "You guessed ", guessInt, " right on your guess nro: ", nroOfGuesses
            break
        elif guessInt < x:
            print "Too low, guess again!"
        elif guessInt > x:
            print "Too high, guess again!"
        else:
            print "You were never supposed to get here, go away!"
