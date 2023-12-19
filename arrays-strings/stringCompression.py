"""aabcccccaaa -> a2b1c5a3"""


def str_compress(s):
    # space: O(n)
    # time: O(n)
    map = {}
    result = ""
    for i in s:
        if i in map:
            map[i] += 1
        else:
            map[i] = 0
    for key in map:
        result += i+str(map[key])
    return result
