# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

import random


# returns new list without duplicates (removed using loop)
def remove_duplicates_loop(list):
    no_duplicates = []
    for i in list:
        if i not in no_duplicates:
            no_duplicates.append(i)
    return no_duplicates


# returns new list without duplicates (removed using sets)
def remove_duplicates_sets(list):
    no_duplicates = set(list)
    return no_duplicates


# Exercise 5 using sets in a different function
# New list out of two removing duplicates
def ex5_with_sets(a_list, b_list):
    common = set(a_list).intersection(set(b_list))
    return common


# making random list with duplicates included
x = [random.randrange(10) for i in range(5)]
print "List x :", (x)
print "List x after duplicates were removed with loop: ", (remove_duplicates_loop(x))
print "List x after duplicates were removed using sets: ", (remove_duplicates_sets(x))

# for ex5 re-making
z = [random.randrange(10) for i in range(5)]
print "List z: ", (z)
print "New common list of x and z without duplicates (using sets): ", (ex5_with_sets(x, z))
