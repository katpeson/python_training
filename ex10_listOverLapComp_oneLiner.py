# http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
# I took base from my code for exercise 5 as it's the same and added just the comprehension as asked
# In here I try to use sets to achieve the whole task in a single comprehension line!

import random

# Trying to include creation of random lists within the comprehension line with using sets
# TODO: I did not see this as result from anyone in comments of the task, is there a reason why to not do it this way?
common = set(random.sample(range(50), 20)).intersection(set(random.sample(range(30), 8)))
print list(common)

# print "Just for comparison creating the lists and printing common for QA: "
# a = random.sample(range(50), 20)
# b = random.sample(range(30), 8)
# common2 = []
# common2 = [i for i in a if i in b and i not in common]
#
# print (a)
# print (b)
# print (common2)

