# Problem Set 1.1
# Name: Antonio Gonzalez
# Collaborators: None
# Time: 1:51 hours


from math import *


current_number = 2
prime_counter = 1

x = input ("How many primes do you want me to produce?")

prime_wanted = x

while (prime_counter < prime_wanted):
	if current_number % 2.0 != 0:
		divisor = current_number - 1
		while (divisor >= 1):
			if divisor == 2:
				print "you have hit a prime " + str(current_number) + " is the " + str(prime_counter) + " prime"
				prime_counter = prime_counter + 1
				divisor = divisor - 1
			elif current_number % divisor != 0:
				divisor = divisor - 1 
			else:
				divisor = 0
	current_number = current_number + 1
raw_input ("program has finished")

