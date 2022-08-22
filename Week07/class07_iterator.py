# iterators
# the use of iterator is to track where you are

s = [3, 4, 5]
t = iter(s)
next(t) "3, then 4, then 5"

d = {'one': 1, 'two': 2, 'three': 3}
d['zero'] = 0
k = iter(d.keys()) # or iter(d), give the same effect
next(k) "'one', 'two', 'three', 'zero'"
v = iter(d.values())
next(v) "1, 2, 3, 0"
i = iter(d.items())
next(i) "('one': 1), ..." # tuples

"iterator in for statement will advance"
r = range(3, 6) # r is an iterable item
ri = iter(r) # ri is an iterator
next(ri) "3" # call next(ri) once, and 3 is passed
for i in ri:
    print(i) "4 5" # becauce 3 is passed, if operated again, nothing got printed out

s1 = [1, 2, 3, 4]
s2 = ['a', 'b', 'c', 'd']
z = zip(s1, s2) # zip(iterable_1, iterable_2)
list(z) "[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]"

def double(x):
    print('**', x, '==>', 2*x, '**')
    return 2*x

m = map(double, range(3,7)) # nothing got doubled until we call them
f = lambda x: x >= 10
fi = filter(f, m)
next(fi)
"""
** 3 ==> 6 **
** 4 ==> 8 **
** 5 ==> 10 **

10"""

t = [1, 2, 3, 2, 1]
reversed(t) "<list_reverseiterator at 0x1115e9c00>"
reversed(t) == t "False" # you cannot campare an interator to a list
list(reversed(t)) == t "True"

def palindrome(s):
    """return true if a list is equal to its reversed self"""
    return all([a == b for a,b in zip(s, reversed(s))])

s = ['hanah']
palindrome(s)
