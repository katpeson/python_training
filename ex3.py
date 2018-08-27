print "What is your name?"
name = raw_input()
print "And your age?"
age = raw_input()
print "So you are %s and you are %s years old?" % (name, age)
print "Did I get it right (yes or no)?"
answer = raw_input("> ")
if answer == "yes" or answer == "Yes":
	print "Yes!"
elif answer == "no" or answer == "No":
	print "No? :("
else:
	print "You can't seem to follow instructions %s. Bye!" % name
