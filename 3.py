'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def largest_prime_factor(n):
	# loop through nums up to n  and check if divisible
	# is prime number
	curr_largest = 1
	for i in range(n):		
		if i in primesSieve(n) and i % n == 0 and i > curr_largest:
			curr_largest = i			

	return curr_largest

def primesSieve(limit):
	lst = range(2, limit)
	for i in range(2, int(math.sqrt(limit)+1)):
		lst = filter(lambda x: x == i or x % i, lst) # Sieve
	return lst

if __name__ == '__main__':
	print largest_prime_factor(600851475143)