def double_eights(n):
    a = 1
    while n - a >= 0:
        if identify(n, a) == 8:
            a = a * 10
            if identify(n, a) == 8:
                return True
            else:
                a = a #一开始写的是 return, 这样的话程序就直接结束了，不对
        else:
            a = a * 10
    return False

def identify(x, a):
    return x % (10 * a) // a
