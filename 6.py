'''
https://projecteuler.net/problem=6
'''
def sol():
    print sumOfSquares(100), squareOfSum(100)
    return squareOfSum(100) - sumOfSquares(100)

'''
Sigma [(n**2) from 1 to n]
'''
def sumOfSquares(n):
    sum = 0
    for num in range(1,n+1):
        sum += (num ** 2)

    '''
    list comprehension:
    sum([n**2 for n in range(1, n+1)])
    '''

    return sum


'''
[sigma(n) from 1 to n] ** 2
'''
def squareOfSum(n):
    sum = 0
    for num in range(1,n+1):
        sum += num

    '''
    list comprehension
    sum(range(1, n+1))**2
    '''
    return sum ** 2

if __name__ == '__main__':
	print "Project Euler Problem 6: Sum of Squares"
	print sol()
