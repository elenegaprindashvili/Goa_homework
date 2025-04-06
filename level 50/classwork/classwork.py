def is_isogram(string): 
    string = string.lower()  
    lowered_letters = set()  
    for char in string:
        if char in lowered_letters:
            return False
        lowered_letters.add(char)
    return True 


