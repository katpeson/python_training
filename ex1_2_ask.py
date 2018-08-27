# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = raw_input("What's your name? ")
age = int(raw_input("How old are you? "))
year = str((2018-age)+100)
print (name + " will be 100 years old in the year " + year)
repeat = int(raw_input("Give a random number: "))
print(("You will turn 100 years old in " + year + "\n") * repeat)