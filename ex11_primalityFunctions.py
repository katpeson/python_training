# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# I took base from my code for exercise 4 as it's the same task and added just the function usage as asked
# TODO: I could also make printing function instead of doing it in main


def get_number(prompt="Give me a number:"):
    return int(input(prompt))


def is_prime(int):
    if int == 1 or int == 0:
        return False
    elif int == 2:
        return True
    else:
        # because any number divides by 1 and itself so excluding those, and biggest divider anyway
        # could be 1/2 of the number?
        possible_dividers = range(2, (int/2)+1)
        print (possible_dividers)
        for i in possible_dividers:
            # print "i is ", i
            # divider_option = int % i
            # print divider_option
            if int % i == 0:
                return False
        return True


number = get_number()
# just so I get it for printing
result = is_prime(number)

if result:
    print " Congratulation, number %d is a Prime!" % number
else:
    print "Number %d is not a Prime, but composer" % number

print "The end"

