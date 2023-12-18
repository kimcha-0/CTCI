"""Replace all whitespace with '%20'"""


def urlIFY(s, length):
    result = ""
    for i in range(length):
        if s[i] == ' ':
            result.append('%20')
        else:
            result.append(s[i])
    return result
