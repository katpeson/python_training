# http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
# Write a function that takes an ordered list of numbers (a list where the elements are in order...
# from smallest to largest) and another number. The function decides whether or not the given number...
# is inside the list and returns (then prints) an appropriate boolean.
#
# Extras:
# Use binary search

import random


# Creating sorted list of random integers
# :param length is the wanted length of the list
# :param max_value is the highest integer value wanted from random integers in list
# :return created sorted list
def create_sorted_list(length, max_value):
    sorted_list = []
    while len(sorted_list) < length:
        random_number = random.randint(0, max_value)
        '''
        If to excluding duplicate list entries but making sure list is still
        created as long as 'length' indicates
        '''
        if random_number not in sorted_list:
            sorted_list.append(random_number)
    sorted_list.sort()
    return sorted_list


# Checks if can find given number from the given list
# :param list_a is given list of integers to check
# :param nro is given integer to find from the list
# :return True if nro is found from list and False if it's not there
def in_list(list_a, nro):
    try:
        list_a.index(nro)
        return True
    except ValueError:
        return False


# Does the same job as in_list() above but using binary search
# :param list_a is given list of integers to check
# :param nro is given integer to find from the list
# :return True if nro is found from list and False if it's not there
# TODO this gets stuck when length or middle gets too low! and returns None only
def binary_list_search(list_a, nro):
    length = len(list_a)
    print "length is ", length
    while length > 1:
        middle = len(list_a)//2
        if middle > 1:
            print "middle is ", middle
            if list_a[middle] > nro:
                list_a = list_a[:middle-1]
                length = len(list_a)
                print "length is ", length
            elif list_a[middle] < nro:
                list_a = list_a[middle+1:]
                length = len(list_a)
                print "length is ", length
    if length < 1:
        return False
    else:
        return True


# main to run the task
if __name__ == "__main__":
    max_int = 15
    list_length = 8
    list_c = create_sorted_list(list_length, max_int)
    print "Sorted list is: ", list_c
    number = random.randint(0, max_int)
    print "Number to find is: ", number
    # print "Search with list index method -->"
    # print "Number found in sorted list? "
    # print in_list(list_c, number)
    print "Search with binary search method -->"
    # print "Number found in sorted list? "
    print binary_list_search(list_c, number)
