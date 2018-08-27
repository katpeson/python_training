alist = raw_input("Give me a string: ")
x = len(alist)
blist = []
i=0
while i < x:
	blist.append(alist[x-1])
	x = x-1
	
str_blist = ''.join(blist)
if alist == str_blist:
	print "YES! The string you gave me is a palindrome!"
else:
	print "NO, String you gave me is not a palindrome"