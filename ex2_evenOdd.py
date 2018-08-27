# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

check = int(raw_input("Give me the first number: "))
number = int(raw_input("Give me the second number:"))

# test for odd or even and additional step to check if the number is the multiply of 4 
# disabled since made last additional step to ask two numbers (check & number)!
#if (number % 2) == 0:
#	if (number % 4) == 0:
#		print "%d is an even number that can be divided by 4" % number
#	print "%d is an even number" % number
#else:
#	print "%d is an odd number" % number

if (check % number) == 0:
	print "Your first number %d can be evenly divided with your second number %d!" % (check, number)
else:
	print "Number %d cannot be evenly divided with %d" % (check, number)	
