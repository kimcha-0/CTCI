"""aabcccccaaa -> a2b1c5a3"""


def str_compress(s):
    # space: O(n)
    # time: O(n^2) when accounting for string concatenation in python
    # time: O(n) when using array and joining
    map = {}
    result = []
    for i in s:
        if i in map:
            map[i] += 1
        else:
            map[i] = 0
    for key in map:
        result.append(key)
        result.append(str(map[key]))
    return ''.join(result)


print(str_compress('aabcccccaaa'))
