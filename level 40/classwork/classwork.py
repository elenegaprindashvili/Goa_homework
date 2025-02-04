# def password(st):
#     if (len(st) < 8):
#         return False
#     is_uper = False
#     is_lower = False
#     is_digit_num = False
    
#     for char in st:
#         if char.isdigit():
#             is_digit_num = True
#         if char.is_lower():
#             is_lower = True
#             if char.isupper():
#                 is_uper = True
#                 return is_uper and is_lower and is_digit_num



    

def is_isogram(string): 
    lowerd_string = string.lower()
    for char in lowerd_string:
         if lowerd_string.count(char) > 1:
             return False
    return True

def friend(x):
    list_friends = []
    for i in x:
        if len(i) == 4:
            list_friends.append(i)
            return list_friends
        
def validate_pin(pin):
    if not pin.isdigit():
        return False
    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
    
