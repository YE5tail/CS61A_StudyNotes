# representation

"""v = print(repr(v))"""

# value
>>> 12e12
12000000000000.0
>>> print(repr(12e12)) # equals to 12e12
12000000000000.0

# string
>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> half
Fraction(1, 2)
>>> repr(half)
'Fraction(1, 2)'
>>> str(half)
'1/2'
>>> print(half)
1/2
>>> eval(repr(half))
Fraction(1, 2)

>>> s = 'hello, world'
>>> print(repr(s))
'hello, world'
>>> str(s)
'hello, world'
>>> repr(repr(repr(s)))
'\'"\\\'hello, world\\\'"\'' # python used back slash to indicate where '' ends
>>> eval(eval(eval(repr(repr(repr(s))))))
'hello, world'
>>> eval(s)
NameError: name 'hello' is not defined # hello, world is not a valid python expression

# F-string

>>> from math import pi
>>> 'Pi starts with ' + str(pi) + '...'
'Pi starts with 3.141592653589793...' # can be written using f-string...
>>> f'Pi starts with {pi}...'
'Pi starts with 3.141592653589793...' # {} is treated as a python expression
>>> f'2 + 3 = {3 + 2}'
'2 + 3 = 5'
>>> f'2 + 2 = {(lambda x: x + x)(2)}'
'2 + 2 = 4'

# special method names, which have built-in behavior
# __init__
# __repr__: invoked to display an object as a python expression
# __add__
# __bool__
# __float__

>>> one, two, zero = 1, 2, 0
>>> one.__add__(two) # equal to one + two
3
>>> one.__bool__() # equal to bool(one)
True
>>> zero.__bool__()
False
