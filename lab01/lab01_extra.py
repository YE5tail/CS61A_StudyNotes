"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1
    else:
        a, total = 1, n
        while a < k:
            total = total * (n-a)
            a += 1
        return total

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
    a = 1
    while n - a >= 0:
        if n % (10 * a) // a == 8:
            a = a * 10
            if n % (10 * a) // a == 8:
                return True
            else:
                a = a
        else:
            a = a * 10
    return False