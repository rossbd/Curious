# curious5.py
#
# This is quick python hack to find all "curious" sequences for n=5.
# Because of the self-referencing definition of a curious sequence, the 'if' statement is clumsy.
# This tool can be generalized to the n case, but high n has a low number of solutions.
# Read more about curious sequences at: https://www.maa.org/sites/default/files/Curious_Sequence-Baily_and_Lautzenheiser40999.pdf
#
# Brandon Ross - 2015

# the product() function makes life easy; there are many ways to do this. 

from itertools import product

# generate the the entire space of sequences for n=5
# (to generalize to the case of 'n', change the '5's below to your choice of 'n'.)
li = list( product(range(0, 5), repeat=5) )

# This for loop tests all possible sequences in the set of sequences for any arbitrary n
for i in range( len(li) ):

	# Test whether each sequence in the space is "curious"
	# A sequence is curious when the number of times a value occurs in a sequence (the left side) = the value at that particular index (the right side)
	# from this, to generalize up, add more li[i].count()s to the left-hand side.
	if tuple([li[i].count(0), li[i].count(1), li[i].count(2), li[i].count(3), li[i].count(4) ]) == tuple(li[i]):
		
		# print any curious sequence (if any--solutions not guaranteed for arbitrary 'n')
		print li[i]

