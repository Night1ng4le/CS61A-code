def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    for i in range(n):
        temp = n
        if n % (i + 1) == 0:
            # print(i+1)
            if n // (i + 1) != temp:
                return n // (i + 1)
    return 1
        
if __name__ == '__main__':
    print(largest_factor(15))