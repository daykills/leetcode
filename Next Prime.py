"""
Given a number, return the next smallest prime number

Note: A prime number is greater than one and has no other factors other than 1 and itself.

"""
"""
understand:
- is there guaranteed to be a solution?
- is the input number guaranteed to be positive?
- what makes a number prime? what does this number have to satisfy?

edge case: 
input: -1
output: 2

match: general math problem

plan: Given a number n, the largest factor of n is √n. This should imply, the loop to find if a number is prime should stop at √n.


"""

def next_prime(n):
    if n < 2: return 2

    n += 1

    while True:
        if is_prime(n):
            return n
        n += 1

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return False
    for i in range(4, int(n**0.5)):
        if n % i == 0:
            return False
    return True