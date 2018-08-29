# http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
# I took base from my code for exercise 5 as it's the same and added just the comprehension as asked

import random
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(50), 20)
b = random.sample(range(30), 8)
# common = set(a).intersection(set(b)) #clean version of the below
common = []
# common2 = []
# this below I try to fit in one line
# for i in a:
#     if i in b and i not in common2:
#         common2.append(i)

common = [i for i in a if i in b and i not in common]

print (a)
print (b)
print (common)
# print (common2)
