from math import sqrt, pow
from re import compile


def NumberOfPointsMatching():
    """Determines number of matching points"""
    matchings = 0
    points = []
    n = r = False
    coordinate_p = compile(r"^\d+ \d+$")
    n_p = compile(r"^\d+$")
    distanceToLookFor = float(2018)

    # number of points input and verification
    while not n:
        n_inp = input("Enter the number of points: ")
        if n_p.match(n_inp):
            int_n_inp = int(n_inp)
            if int_n_inp > 0 and int_n_inp <= 10**5:
                n = r = int_n_inp
    # coordinates input and verification
    while n > 0:
        p_inp = input("Enter coordinates in pos "+str(r-n+1)+": ")
        if coordinate_p.match(p_inp):
            splitted_p_inp = p_inp.split(" ")
            if int(max(splitted_p_inp)) < 2**31:
                points.append(splitted_p_inp)
                n -= 1
    # evaluating distances and incrementing matching points in case distance is 2018
    i = 1  # in order to slice points from next element to end of list
    for point in points:
        nextPoints = points[i:]
        if r - i > 0:
            for nextPoint in nextPoints:
                if calcDistanceBetweenPoints(point, nextPoint) == distanceToLookFor:
                    matchings += 1
            i += 1

    return matchings


def calcDistanceBetweenPoints(A, B) -> int:
    """Determines distance between point A = [xa, ya] and B = [xb, yb]"""
    xa, ya = int(A[0]), int(A[1])
    xb, yb = int(B[0]), int(B[1])
    return sqrt(pow(xa-xb, 2) + pow(ya - yb, 2))


print(NumberOfPointsMatching())
