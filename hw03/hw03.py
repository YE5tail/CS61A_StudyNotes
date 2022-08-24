HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos == 0:
        return 0
    elif pos%10 == 8:
        return 1 + num_eights(pos//10)
    else:
        return num_eights(pos//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return pingpong(n-1) + dir(n)

def dir(n):
    if n < 8:
        return 1
    elif num_eights(n-1) or (n-1) % 8 == 0:
        return 0 - dir(n-1)
    else:
        return dir(n-1)

#上面一个代码不是最优解，因为会重复循环dir(n)和num_eights(n)。
#当时纠结的点在于如何track方向，实际上用下述代码的step就可解决。不要僵化使用 f(n-1)。
#高阶函数return的是另一个函数，不是a+b，否则没有意义。

def pingpong_alt(n):
    def helper(result, i, step):
        if n == i:
            return result
        elif num_eights(i) or i % 8 == 0:
            return helper(result - step, i + 1, -step)
        else:
            return helper(result + step, i + 1, step)
    return helper(1, 1, 1)

pingpong_alt(17)

def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(change, i):
        if change == 0:
            return 1
        elif change < 0:
            return 0
        elif i == 1:
            return 1
        else:
            return helper(change-i, i) + helper(change, get_smaller_coin(i))
    return helper(change, 25)
"""
def count_coins_alt(change):
    def helper(change, i):
        if change == 0:
            return 1
        elif change < 0:
            return 0
        elif i == 25 and change % i == 0:
            return 1
        elif i == 25:
            return 0
        else:
            return helper(change-i, i) + helper(change, get_larger_coin(i))
    return helper(change, 1)
"""
