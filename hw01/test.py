def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    n = str(n)
    # print(n)
    if len(n) < 2:
        return False
    for i in range(len(n)):
        if n[i] == '8':
            if n[i+1] == '8':
                return True
    return False
        
if __name__ == '__main__':
    

