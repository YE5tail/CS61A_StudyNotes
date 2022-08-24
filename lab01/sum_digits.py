def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    a, sum = 1, 0
    while n - a >= 0:
        sum = sum + n % (10 * a) // a
        a = a * 10
    return sum

sum_digits(26)

10 % 10 // 1#4
10 % 100 // 10 #3
13 % 1000 // 100 #2



123 // 1000
a, b, c
