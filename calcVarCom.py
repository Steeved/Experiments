from re import search as s, sub


def factorial(n):  # returns the amount or ways to arrange n elements -  n!
    m = 1
    for v in range(1, n + 1):
        m *= v
    return m


def variation(n, k):  # returns the amount of ways to arrange n elements in k places - n!/(n-k)!
    if k > n:
        print('\n!!! Error - k Cannot be greater than n in var(n, k) !!!\n')
    return factorial(n) / factorial(n - k)


def combination(n, k):  # returns the amount of ways to select k elements from n elements - n!/(n - k)!k!
    if n < k:
        print('\n!!! Error - k Cannot be greater than n in com(n, k) !!!\n')
    else:
        print(n, k, variation(n, k), factorial(k))
        return variation(n, k) / factorial(k)


# replacement of eval(); its done in 3 stages:
# replacement of parts of the string(expression)
# with the result of the function specified - factorial, variation, combination.
def evaluateexp(exp):
    factre = 'fact\\(([0-9]+)(\\))'
    varre = 'var\\((\\d+)(, )(\\d+)(\\))'
    comre = 'com\\((\\d+)(, )(\\d+)(\\))'
    res = exp
    if s(factre, res):
        res = sub(factre, str(factorial(int(s(factre, res).group(1)))), res)
    if s(varre, res):
        res = sub(varre, str(variation(int(s(varre, res).group(1)), int(s(varre, res).group(3)))), res)
    if s(comre, res):
        res = sub(comre, str(combination(int(s(comre, res).group(1)), int(s(comre, res).group(3)))), res)
    return res


expression = input('Expression: ')
input(evaluateexp(expression))
