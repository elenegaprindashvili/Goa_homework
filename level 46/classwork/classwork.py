def filter_list(l):
    'return a new list with the strings filtered out'
    result = []
    for item in l:
        if type(item) != str:
            result.append(item)
    return result

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = []
    for char in string_:
        if char not in vowels:
            result.append(char)
    return ''.join(result)