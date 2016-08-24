'''
Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20..
Example: 2520 is one such number that is evenly divisible by all numbers from 1 to 10.
'''

'''
Needs to be divisible by the primes from 1 to 20
2,3,5,7,11,13,17,19

Brute force:
Loop through all nums from 21 and check if divisible by the above numbers

Math:
2*3*5*7*11*13*17*19
2**n < 20m n=4
3**n < 20, n=2

'''
def sol():
	return 2**4 * 3**2 * 5*7*11*13*17*19


if __name__ == '__main__':
	print "Project Euler Problem 5: Smallest Multiple"
	print sol()

