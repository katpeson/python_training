# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# ...strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols!
# TODO ask user for the length of the needed pw and pass that on!
# TODO extra: Ask the user how strong they want their password to be. For weak, pick a word or two from a list.

import random
import string


# asking user for security level of the needed password
def get_strength(prompt="Level: "):
    print "Enter level of your password security from 1 (weak) to 3 (strong)"
    answer = ""
    while not answer:
        try:
            answer = int(raw_input(prompt))
        except ValueError:
            print("That's not a number! Try again: ")
    return answer


# creates random pw every time called out and returns pw
# For level 1: gives 6 random letters (lower & upper case)
# For level 2: gives 8 random characters or digits and shuffles those a bit more
# For level 3: First creates random list of 3 of each needed character type
#              Then creates random pw out of those random lists to making sure all types of char are included
def provide_password(level):
    if level == 1:
        return random.sample(string.letters, 6)
    elif level == 2:
        return random.sample(shuffle_items(list(string.letters + string.digits)), 8)
    # level 3 is the original solution to this task without 'extra'
    elif level == 3:
        lower_case_letters = random.sample(string.ascii_lowercase, 3)
        upper_case_letters = random.sample(string.ascii_uppercase, 3)
        numbers = random.sample(string.digits, 3)
        symbols = random.sample(string.punctuation, 3)
        password = lower_case_letters + upper_case_letters + numbers + symbols
        random_password = shuffle_items(password)
        return random_password
    else:
        return "You did not give acceptable security level (1-3), password was not created"


# mixes the selected random items up within the list
def shuffle_items(list):
    new = []
    x = len(list)
    while x != 0:
        i = random.randint(0, x-1)
        new.append(list.pop(i))
        x -= 1
    return new


# make a string out of a list
def to_string(list):
    return ''.join(list[::])


print to_string(provide_password(get_strength()))

