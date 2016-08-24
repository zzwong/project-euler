import math

'''
Brute Force:
loop through 3 digit numbers 100 to 999 and multiply them
check if palindrome
O(n**2)
'''
def largest3digit_palindrome():
	largest = 0
	for i in range(100,999):
		for j in range(100, 999):
			tmp_product = i * j
			if is_palindrome(tmp_product):
				if tmp_product > largest:
					largest = tmp_product
	return largest	

def is_palindrome(n):
	num_to_str = str(n)
	digits_to_check = int(math.floor(len(num_to_str)/2))
	a = 0
	b = len(num_to_str)-1
	for i in range (0, digits_to_check):
		if num_to_str[a] != num_to_str[b]:
			return False
		a+=1
		b-=1
	return True

if __name__ == '__main__':
	print largest3digit_palindrome()
	'''
	print "testing is_palindrome()"
	print "should be true. result:", is_palindrome(1001)
	print "false. result: ", is_palindrome(2001)
	print "true. result: ", is_palindrome(23032)
	print "false. result: ", is_palindrome(23011)
'''
# 906609
