def remove_duplicate_words(s):
    words = s.split() 
    result = []  

    for word in words:
        if word not in result: 
            result.append(word)  

    return ' '.join(result)  


def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
        

def factorial(n):
    if n == 0: 
        return 1
    else:
        return n * factorial(n - 1)  