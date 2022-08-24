# generator

def plus_minus(y):
    yield y
    yield -y

g = plus_minus(5)
next(g)

def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

# processed lazily, won't go through while loop unless it gests called next
t = evens(1, 10)
next(t)

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'BOOOMMMMM'

t = countdown(5)
next(t)

def prefix(s):
    if s:
        yield from prefix(s[:-1])
        yield s

list(prefix('both')) "['b', 'bo', 'bot', 'both']"

def substrings(s):
    if s:
        yield from prefix(s)
        yield from substrings(s[1:])

list(substrings('both')) "['b', 'bo', 'bot', 'both', 'o', 'ot', 'oth', 't', 'th', 'h']"

def patitions(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in patitions(n-m, m)]
        without_m = patitions(n, m-1)
        return exact_match + with_m + without_m

for i in patitions(6, 4): print(i)
"""
2 + 4
1 + 1 + 4
3 + 3
1 + 2 + 3
1 + 1 + 1 + 3
2 + 2 + 2
1 + 1 + 2 + 2
1 + 1 + 1 + 1 + 2
1 + 1 + 1 + 1 + 1 + 1
"""

# write patitions function using generator
def patitions_gen(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in patitions_gen(n-m, m):
            yield p + ' + ' + str(m)
        yield from patitions_gen(n, m-1)

t = patitions_gen(6, 4)
next(t)

# using generator can be dramatically efficient and fast if the result is huge
# but you only want a few of results
# for example: patitions_gen(60, 50)
