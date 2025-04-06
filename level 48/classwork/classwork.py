def xo(s):
    return s.lower().count("x") == s.lower().count("o")

def find_short(s):
    words = s.split()
    short_word = words[0]
    for word in words: 
        if len(word) < len(short_word): 
            short_word = word
    return len(short_word)

def solution(text, ending):
        return text[-len(ending):] == ending
