"""Given two strings, determine if one is a permutation of the other"""


def checkPerm(s, t):
    # use map to construct freq table for each string
    # and check to see if they are equal

    if len(s) != len(t):
        return False

    mapOne = {}
    mapTwo = {}

    for i in range(len(s)):
        mapOne[s[i]] = 1 + mapOne.get(s[i], 0)
        mapTwo[t[i]] = 1 + mapTwo.get(t[i], 0)

    for key in mapOne:
        if mapOne[key] != mapTwo[key]:
            return False

    return True
