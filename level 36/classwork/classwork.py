def digitize(n):
    reversed_res = []
    n- str(n)[::-1]
    for i in str(n):
        reversed_res.append(int(1))
        return reversed_res

def is_anagram(test, original):
    test = test.lower().replace(" ", "")
    original = original.lower().replace(" ", "")
    return sorted(test) == sorted(original)


def get_count(s):
    vowels =("a", "e", "i", "o", "u")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            return count
        

def filter_list(l):
    'return a new list with the strings filtered out'
    return [item for item in l if type(item) != str]




