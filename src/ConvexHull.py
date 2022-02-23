import math


def CheckLocation(p1, p2, p3):
    return p1[0] * p2[1] + p3[0] * p1[1] + p2[0] * p3[1] - p3[0] * p2[1] - p2[0] * p1[1] - p1[0] * p3[1]


# def MaxMinId(S, max, min):
#     for i in range(1, len(S)):
#         if(S[i][0] > S[max][0]):
#             max = i
#         if(S[i][0] < S[min][0]):
#             min = i

def DivideArea(p1, pn, S, S1, S2):
    for p in S:
        det = CheckLocation(p1, pn, p)
        if det > 0:
            S1.append(p)
        elif det < 0:
            S2.append(p)


def Angle(d1, d2):
    if(d1 == 0 or d2 == 0):
        return 0
    else:
        if(d1 > d2):
            return math.acos(d2/d1)
        else:
            return math.acos(d1/d2)


def FurthestDistance(S, p1, pn):
    maxd1 = math.dist(S[0], p1)
    maxd2 = math.dist(S[0], pn)
    index = 0

    for i in range(1, len(S)):
        d1 = math.dist(S[i], p1)
        d2 = math.dist(S[i], pn)
        if (d1 + d2 > maxd1 + maxd2):
            index = i
            maxd1 = d1
            maxd2 = d2
        elif (d1 + d2 == maxd1 + maxd2):
            if (Angle(d1, d2) > Angle(maxd1, maxd2)):
                index = i
                maxd1 = d1
                maxd2 = d2
    return S.pop(index)


def ConvexHullDnC(S):
    hull = []
    S1 = []
    S2 = []
    S = sorted(S, key=lambda x: x[0])
    p1 = S.pop(0)
    pn = S.pop(-1)
    hull.append([p1, pn])
    for p in S:
        det = CheckLocation(p1, pn, p)
        if det > 0:
            S1.append(p)
        elif det < 0:
            S2.append(p)
    FindHull(S1, p1, pn, hull)
    FindHull(S2, pn, p1, hull)
    return hull


def FindHull(S, p1, pn, hull):
    if(len(S) == 0):
        hull.append([p1, pn])
    else:
        S1 = []
        S2 = []
        pmax = FurthestDistance(S, p1, pn)
        for p in S:
            det1 = CheckLocation(p1, pmax, p)
            if det1 > 0:
                S1.append(p)
            det2 = CheckLocation(pmax, pn, p)
            if det2 > 0:
                S2.append(p)
        FindHull(S1, p1, pmax, hull)
        FindHull(S2, pmax, pn, hull)
