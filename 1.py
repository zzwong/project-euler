'''
Multiples of 3 and 5 

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def loop_sol():
	'''
	returns sum of all multiples of 3 or 5, below 1000.
	runtime: O(N)
	'''
	ret = 0
	for i in range(1000):
		if i % 3 ==0  or i % 5==0:
			ret += i

	return ret

if __name__ == '__main__':
	print 'Sum of all multiples of 3 or 5 below 1000:' ,loop_sol()

# 233168
