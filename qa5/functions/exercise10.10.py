def opposite_str(str):
    result = ''
    for i in range(len(str)-1, -1, -1):
        result += str[i]
    return result


def cut_spaces(str):
    result = ''
    for i in str:
        if i != ' ':
            result += i
    return result


def isPolindrom(str: str):
    str = cut_spaces(str)
    opposite = opposite_str(str)
    if opposite == str:
        return True
    else:
        return False

print(isPolindrom(input("enter string: ")))
