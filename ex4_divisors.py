# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(raw_input("Give me a number to work with: "))
list = range(1,number+1)
divisors = []
for i in list:
	if (number % i) == 0:
		divisors.append(i)
	
print "The divisors of the given number are: %s" % (divisors)

