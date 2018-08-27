number = int(raw_input("Give me a number: "))
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
small = []
for i in list:
	if i < number:
		small.append(i)
		
print (small)