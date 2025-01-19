def filter_list(l):
    'return a new list with the strings filtered out'
    return [item for item in l if not type(item) == str]



def square_digits(num):
    result = ""
    for digit in str(num):
        result += str(int(digit) ** 2)
    return int(result)


def solution(text, ending):
    return text.endswith(ending)