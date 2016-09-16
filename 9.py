'''
Special Pythagorean Triplet
9



Pythagorean Triplet is a set of 3 natural nums, a<b<c s.t.
				a**2 + b**2 = c**2 


find a*b*c s.t. a+b+c=1000
'''


'''
For each triplet, find one such that the sum of the triplet is 1000
'''

def sol():
	for i in range(1,500):
		for j in range(i,500):
			for k in range(j,500):
				_sum = i+ j + k
				if _sum == 1000 and is_pythagorean_triplet(i,j,k):					
					return i*j*k

def is_pythagorean_triplet(a,b,c):
	if a**2 + b**2 == c**2:
		return True
	return False


if __name__ == '__main__':
	print sol()