def palindrome (stringa):
	if stringa[0] != stringa[-1]:
		print "Sorry not palindrome"
		return
	else: 
		if len(stringa) <= 1:
			print "this is a palindrome"
		else:
			stringa = stringa[1:-1]
			palindrome(stringa)

