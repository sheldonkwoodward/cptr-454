# sheldon woodward
# 1/31/18

import math
from random import randint


def closest_pair(p, q):
    n = len(p)
    if n <= 3:
        if n == 2:
            return math.sqrt(((p[0][0] - p[1][0]) ** 2) + ((p[0][1] - p[1][1]) ** 2))
        else:
            d1 = math.sqrt(((p[0][0] - p[1][0]) ** 2) + ((p[0][1] - p[1][1]) ** 2))
            d2 = math.sqrt(((p[0][0] - p[2][0]) ** 2) + ((p[0][1] - p[2][1]) ** 2))
            d3 = math.sqrt(((p[2][0] - p[1][0]) ** 2) + ((p[2][1] - p[1][1]) ** 2))
            return min(d1, d2, d3)
    pl = p[:math.ceil(n / 2)]
    pr = p[math.ceil(n / 2):]
    ql = p[:math.ceil(n / 2)]
    qr = p[math.ceil(n / 2):]
    dl = closest_pair(pl, ql)
    dr = closest_pair(pr, qr)
    d = min(dl, dr)
    m = p[math.ceil(n / 2) - 1][0]
    s = list()
    for point in q:
        if abs(point[0] - m) < d:
            s.append(point)
    dminsq = d**2
    for i in range(len(s) - 1):
        k = i + 1
        while k <= len(s) - 1 and (s[k][1] - s[i][1]) ** 2 < dminsq:
            dminsq = min(((s[k][0] - s[i][0]) ** 2) + ((s[k][1] - s[i][1]) ** 2), dminsq)
            k += 1
    return math.sqrt(dminsq)


def __main__():
    # generate points list
    points = list()
    print('POINTS')
    for p in range(20):
        points.append((randint(0, 2000) / 100, randint(0, 2000) / 100))
        print(f'  {points[-1]}')
    p = sorted(points, key=lambda x: x[0])
    q = sorted(points, key=lambda y: y[1])
    answer = closest_pair(p, q)
    print(f'Answer: {answer}')


if __name__ == '__main__':
    __main__()
