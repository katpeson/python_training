# http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
# Not sure if giving 5555 should provide 1 cow and 3 bulls when the random only has one time number 5 in it (like 1522)
# --> but for now it does!

import random


# asks user for the 4-digit number and only accepts integer
def get_number(prompt="Give me 4-digit number: "):
    user_input = ''
    while not user_input:
        try:
            user_input = int(raw_input(prompt))
            if check_digits(user_input):
                return str(user_input)
            else:
                user_input = ''
        except ValueError:
            print("That's not a number OR you didn't give me 4-digit number! Try again.")


# checks if the given number is 4-digits or not
def check_digits(number):
    if number < 1000 or number > 9999:
        return False
    else:
        return True


# takes random and the user number and provides cows and bulls respectively
def count_cows(random_number, user_number):
    # not sure if the below if is even needed anymore (probably not)
    if user_number == random_number:
        return [4, 0]
    cows = 0
    bulls = 0
    for i in range(len(user_number)):
        if user_number[i] in random_number:
            if user_number[i] == random_number[i]:
                cows += 1
            else:
                bulls += 1

    return [cows, bulls]


# main to run the task
if __name__ == "__main__":
    guesses = 0
    user_guess = 0
    random_int = str(random.randint(1000, 9999))
    print "Every correct digit in the correct place is a COW and every correct digit in the wrong place is a BULL."
    print random_int
    # printing for testing purposes only
    while user_guess != random_int:
        user_guess = get_number()
        guesses += 1
        cows_bulls = count_cows(random_int, user_guess)
        print "You got %s cow(s) and %s bull(s)" % (cows_bulls[0], cows_bulls[1])
    print "You got the number %s right after %d try / tries" % (random_int, guesses)
