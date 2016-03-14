# Problem Set 1.2
# Name: Antonio Gonzalez
# Collaborators: None
# Time: 00:31

#simple improved program for one value of N

from math import *
import timing


current_sum = 0
n = 20480


current_number = n - 1



while (current_number > 2):
	if current_number % 2.0 != 0:
		divisor = 3
		while (divisor <= current_number):
			if divisor == current_number:
				current_sum = current_sum + log(current_number)
				divisor = current_number + 1
			elif current_number % divisor != 0:
				divisor = divisor + 2 
			else:
				divisor = current_number + 1
	current_number = current_number - 1


print n
print current_sum
print current_sum / n
