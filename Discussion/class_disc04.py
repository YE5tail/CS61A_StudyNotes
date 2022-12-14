"""sequence unpacking
"""
pairs = [[1,2], [2,2], [4,6], [3,3]]
same_count = 0
for x, y in pairs:
    if x == y:
        same_count += 1

same_count

def cheer():
    for _ in range(3):
        print('go trojans!')

cheer()

numerals = {'I': 1, 'V': 5, 'X': 10}
numerals['V']
numerals.keys()
numerals.values()
items = numerals.items( )
dict(items)['V ']

from datetime import date
today = date(2022, 7, 29)
anniversary = date(2019, 4, 30)
str(today - anniversary)

from unicodedata import name, lookup
name('放')
lookup('SNOWMAN')
lookup('soccer ball').encode()

suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()
suits.remove('string')
suits
suits.append('cub')
suits.extend(['sword', 'club'])
suits
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']
suits
original_suits

def f(s=[]):
    """using default mutable objects is dangerous, because it will change.
    """
    s.append(5)
    return len(s)

f()

t = [[1,2],[3,4]]
t[0].append(t[1:2])
t

#***********
#DISC04
#***********

def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    return [fn(i) for i in seq]

def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    return [i for i in seq if pred(i)]

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    """
    i, result = 1, seq[0]
    while i < len(seq):
        result = combiner(result, seq[i])
        i += 1
    return result
    """
    total = seq[0]
    for i in seq[1:]:
        total = combiner(total, i)
    return total

def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    return len(list(filter(lambda x: x.lower()[::-1] == x.lower(), L)))

count_palindromes(("Acme", "Madam", "Pivot", "Pip"))

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * x[i] for i in range(0, len(x), 2)]

from functools import reduce
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        return max(reduce(lambda x, y: x * y, s[::2]),
    reduce(lambda x, y: x * y, s[::3]),
    reduce(lambda x, y: x * y, s[1::3]),
    reduce(lambda x, y: x * y, s[1::2]))
