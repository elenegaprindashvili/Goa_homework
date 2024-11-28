def custom_split(text, delimiter):
    result = []          
    word = ""             
    for char in text:     
        if char == delimiter:  
            if word:            
                result.append(word)   
                word = ""            
        else:
            word += char           
    if word:                   
        result.append(word)     
    return result              





def custom_join(arr, delimiter):
    result = ""
    for i in range(len(arr)):
        result += arr[i]
        if i != len(arr) - 1:
            result += delimiter
    return result

words = ['hello', 'world', 'this', 'is', 'python']
delimiter = " "
print(custom_join(words, delimiter)) 





def custom_replace(text, old, new):
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+len(old)] == old:
            result += new
            i += len(old)  
        else:
            result += text[i]
            i += 1
    return result

text = "hello world"
print(custom_replace(text, "world", "python"))    





def calculator(a, b, operator):
    if operator == "+":
        return a + b
    
a = 5
b = 3
operator = "+"
print(calculator(a, b, operator))  





def create_and_join_words():
    num_words = int(input("1"))
    words = []
    for _ in range(num_words):
        word = input("sky")
        words.append(word)
    joined_words = " ".join(words)
    print("result:", joined_words)
create_and_join_words()




