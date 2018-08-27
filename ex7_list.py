# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

#without comprehension
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# evenlist = []
# for number in a:
# 	if (number % 2 == 0):
# 		evenlist.append(number)
# 	
# print (evenlist)

#and now with comprehension
#with help from https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evenlist = [number for number in a if number % 2 == 0]
print (evenlist)