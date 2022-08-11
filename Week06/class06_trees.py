# Trees
"""
Tree Defination:
- tree has a root label and a list of branches
- each branch is also a tree

>>> tree(3, [tree(1),
             tree(2, [tree(1),
                      tree(1)])])
>>> [3, [1], [2, [1], [1]]]
"""

#*****#
#TREE CONSTRUCTION
#*****#

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees!' # verify the tree defination
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

"""
tree = tree(1, [tree(2, [tree(3)]), tree(3)])
is_leaf(tree )
label(tree)
branches(tree)
"""

"write a fib tree!"

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

f = fib_tree(3)
f

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        count_branches = [count_leaves(b) for b in branches(tree)]
        return sum(count_branches)

count_leaves(f)

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
        """cannot call list(), because argument needs to be iterable!
        list([iterable]), eg list('bear')"""
    else:
        return sum([leaves(b) for b in branches(tree)], [])

leaves(fib_tree(5))

"print a tree"

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

print_tree(fib_tree(4))

# another way of summing leaves in recursion,
# except this time without manipulating the return value of the recursive call
# but only passing on recursive information

# example: instead of writing:
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1) # the muliply is done here

# can be written:
def fact_times(n, k):
    if n == 0:
        return k # when hitting this return, all mutiply has been done
    else:
        return fact_times(n - 1, k * n)

# count how many paths there exit to reach total
def count_paths(t, total):
    if total == label(t):
        found = 1
    else:
        total, found = total - label(t), 0
    return found + sum([count_paths(b, total) for b in branches(t)])

t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1)])

count_paths(t, 7)
