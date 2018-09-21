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


# Checks if can find given number from the given list using list.index()
# :param list_a is given list of integers to check
# :param nro is given integer to find from the list
# :return True if nro is found from list and False if it's not there
def index_search(list_a, nro):
    try:
        list_a.index(nro)
        return True
    except ValueError:
        return False


# Does the same job as in_list() above but using binary search and calls the function recursively
# :param list_a is given ordered list of integers to check
# :param nro is given integer to find from the list
# :return True if nro is found from list and False if it's not there
def binary_search(list_a, nro):
    mid = len(list_a) // 2
    if nro == list_a[mid]:
        return True
    elif len(list_a) == 1:
        return False
    else:
        if nro < list_a[mid]:
            return binary_search(list_a[:mid], nro)
        else:
            return binary_search(list_a[mid+1:], nro)


def search(list_a, nro):
    for i in range(len(list_a)):
        if i >= len(list_a):
            return False
        elif list_a[i] == nro:
            return True
        else:
            i += 1
    return False


# main to run the task
if __name__ == "__main__":
    max_int = 15
    list_length = 8
    list_c = create_sorted_list(list_length, max_int)
    print "Sorted list is: ", list_c
    number = random.randint(0, max_int)
    print "Number to find is: ", number
    print "Search with list index method -->"
    print index_search(list_c, number)
    print "Search with binary search method -->"
    print binary_search(list_c, number)
    print "Search list index by index with loop -->"
    print search(list_c, number)
