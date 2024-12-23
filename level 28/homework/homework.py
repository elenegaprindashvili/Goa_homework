def bool_to_word(boolean):
    # TODO
    return "Yes" if boolean else "No"




def remove_char(s):
    return s[1:-1]


def string_to_number(s):
    return int(s)
print(string_to_number("1234"))  
print(string_to_number("605"))  
print(string_to_number("1405"))  
print(string_to_number("-7"))    

def remove_spaces(x):
    return x.replace(" ", "")
print(remove_spaces("Hello World"))  
print(remove_spaces(" Python is fun "))  
print(remove_spaces("No spaces here"))  
print(remove_spaces("  Remove spaces  "))  


def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1, 5.2, 4, 0, -1]))  
print(sum_of_numbers([]))  
print(sum_of_numbers([-2.398]))  


