"""Check if a given string is a permutation of a palindrome"""


def palindromePermutation(s):
    map = {}
    one_count = 0
    s = s.lower()
    for i in s:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    if len(s) % 2 == 0:
        # frequency table should have all even numbers
        for key in map:
            if map[key] % 2 != 0:
                one_count += 1
                if one_count > 1:
                    return False
    else:
        # frequency table should have all even
        for key in map:
            if map[key] % 2 != 0:
                return False
    return True


print(palindromePermutation('hello'))
print(palindromePermutation('david'))
print(palindromePermutation('sarah'))
print(palindromePermutation('hannah'))
print(palindromePermutation('aaaadd'))
