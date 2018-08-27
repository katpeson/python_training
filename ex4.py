prompt = "> "
print "What's your name?"
name = raw_input(prompt)
print "How old are you?"
age = int(raw_input(prompt))
year_now = 2018
year_100 = year_now + (100 - age)
print "How many times you want the outcome be printed?"
repeat = int(raw_input(prompt))
i = 0
while i < repeat:
	print "I calculated that you will turn 100 years old in year %d %s" % (year_100, name)
	i += 1