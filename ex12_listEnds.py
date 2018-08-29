# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

import random


def top_end(list):
    first_last = []
    first_last.append(list.pop(0))
    first_last.append(list.pop())
    return first_last


a = random.sample(range(120), 10)
print (a)
# printing before first and last removed (was not told to save those!)
print (top_end(a))
