# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(120), k = 10)
b = random.sample(range(101), k = 8)
#common = set(a).intersection(set(b)) #clean version of the below
common = []
for i in a:
	if i in b and i not in common:
		common.append(i)  			

print (a)
print (b)  			
print (common)