# sheldon woodward
# 1/31/18

import math
from random import randint


def closest_pair(p, q):
    """
    Finds the distance between the two closest points in a set of points.

    :param p: The first list of two-tuple points sorted by ascending x-value. Must contain the same points as q.
    :param q: The second lest of two-tuple points sorted by ascending y-value. Must contain the same points as p.
    :return: Returns the distance between the two closest points in the lists.
    """
    # get the number of points
    n = len(p)
    if n != len(q):
        raise ValueError('the length of P and Q do not match')
    # use brute force to solve when there are two or three pairs remaining
    if n <= 3:
        # two pairs remaining
        if n == 2:
            return math.sqrt(((p[0][0] - p[1][0]) ** 2) + ((p[0][1] - p[1][1]) ** 2))
        # three pairs remaining
        elif n == 3:
            d1 = math.sqrt(((p[0][0] - p[1][0]) ** 2) + ((p[0][1] - p[1][1]) ** 2))
            d2 = math.sqrt(((p[0][0] - p[2][0]) ** 2) + ((p[0][1] - p[2][1]) ** 2))
            d3 = math.sqrt(((p[2][0] - p[1][0]) ** 2) + ((p[2][1] - p[1][1]) ** 2))
            return min(d1, d2, d3)
        # one pair remaining, error state
        else:
            raise ValueError('only one point is being compared')
    # divide P into left and right pieces
    pl = p[:math.ceil(n / 2)]
    pr = p[math.ceil(n / 2):]
    # divide Q into left and right pieces
    ql = p[:math.ceil(n / 2)]
    qr = p[math.ceil(n / 2):]
    # recursively call closest_pair on the divided left and right sections
    dl = closest_pair(pl, ql)
    dr = closest_pair(pr, qr)
    # find the minimum point distance returned by each recursive call
    d = min(dl, dr)
    # find all points less than threshold maximum
    m = p[math.ceil(n / 2) - 1][0]
    s = list()
    for point in q:
        if abs(point[0] - m) < d:
            s.append(point)
    d_min_squared = d**2
    # find and return the minimum point distance of all the possible point combinations
    for i in range(len(s) - 1):
        k = i + 1
        while k <= len(s) - 1 and (s[k][1] - s[i][1]) ** 2 < d_min_squared:
            d_min_squared = min(((s[k][0] - s[i][0]) ** 2) + ((s[k][1] - s[i][1]) ** 2), d_min_squared)
            k += 1
    return math.sqrt(d_min_squared)


def __main__():
    # generate points list of length 20
    num_points = 20
    points = list()
    print('POINTS')
    for p in range(num_points):
        points.append((randint(0, 2000) / 100, randint(0, 2000) / 100))
        print(f'  {points[-1]}')
    # sort points into P and Q
    p = sorted(points, key=lambda x: x[0])
    q = sorted(points, key=lambda y: y[1])
    # find the points that are closest together
    answer = closest_pair(p, q)
    print(f'Answer: {answer}')


if __name__ == '__main__':
    __main__()
