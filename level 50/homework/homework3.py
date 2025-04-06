def longest(a1, a2):
    combined_string =a1 + a2 
    letters = []
    for letter in combined_string:
        if letter not  in combined_string:
            letters.append(letter)
            letters.sort()
            result = ""
            for letter in letters:
                result += letter
                return letter