def binConvert(a):
    b = []
    c = a
    while c > 0:
        if c < 2:
            b.append(str(c))
        else:
            b.append(c % 2)
        c -= c % 2
        c //= 2
    e = ''
    for h in b:
        e = e + str(h)
    return e[::-1]


def intConvert(b):
    c = 1
    d = 0
    for g in range(len(str(b)) - 1, -1, -1):
        d += int(str(b)[g]) * c
        c *= 2
    return str(d)

