"""Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?"""


def isUnique(s):
    # brute force Time: O(n^2) Space: O(1)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def isUnique_opt(s):
    # more optimal solution: Time: O(n) Space: O(n)
    map = {}
    for i in range(len(s)):
        if s[i] in map:
            return False
        else:
            map[s[i]] = 1
    return True
