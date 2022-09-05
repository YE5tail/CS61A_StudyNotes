# recursive objects

# linked list class

class Link:
    """link(3, Link(4, Link(5)))"""

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        # isinstance returns if rest is an instance of a class or of a subclass
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

>>> s = Link(3, Link(4, Link(5)))
>>> s.first
3
>>> Link(8, s.rest)
Link(8, Link(4, Link(5)))

def ranged_link(start, end):
    if start >= end:
        return Link.empty
    else:
        return Link(start, ranged_link(start + 1, end))

def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest

def square(x):
    return x * x

def odd(x):
    return x % 2 == 1

>>> r = ranged_link(1, 6)
>>> map_link(square, filter_link(odd, r))
Link(1, Link(9, Link(25)))



def add(v, s): # this is my solution
    """add v to an ordered list with no repeats, and then return modified s,
    if v is already in s, return the original list
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(4, s)
    Link(1, Link(3, Link(4, Link(5))))"""

    if s is Link.empty:
        s = Link(v)
    elif s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v:
        s.rest = add(v, s.rest)
    return s

def add_alt(v, s): # this is provided by John
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and (s.rest is Link.empty):
        s.rest = Link(v)
    elif s.first < v:
        add_alt(v, s.rest)
    return s


class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])
