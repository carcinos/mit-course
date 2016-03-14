###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes

	  # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar

consecutive = 0
can = 0

# If at any point the number is divisible by a//b//c then 
# can goes to 1, and after calculation system understands
# that that number is valid. 
# if none work, then can will remain 0 and so 
# system knows that that number doesnt work

for n in range (1,150):
	for a in range (0,20):
		for b in range (0,20):
			for c in range (0,20):
				if packages[0]*a + packages[1]*b + packages[2]*c == n:
					can = 1
	if can == 0:
		bestSoFar = n
		consecutive = 0
	else:
		consecutive += 1
		can = 0
		if consecutive == 6:
			print str(bestSoFar) + "is the final answer"

