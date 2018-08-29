# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

import random


# Option 1
def top_end1(list):
    first_last = [list[0], list[len(list) - 1]]
    return first_last


# Option 2, will remove the popped items from original list (was not told to save those)!
def top_end2(list):
    first_last = []
    first_last.append(list.pop(0))
    first_last.append(list.pop())
    return first_last


a = random.sample(range(120), 10)
# Printing original list
print (a)
# Result option 1, running this first since option 2 removes the top and end items from original list
print (top_end1(a))
# Result option 2
print (top_end2(a))
