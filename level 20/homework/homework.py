#1
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = sum(1 for letter in letters if letter in vowels)
print(vowel_count)  



#2
numbers = [i for i in range(1, 101) if i % 5 == 0 or i % 3 == 0]

print(numbers)  



#3
mixed_elements = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e']


result_string = (mixed_elements)

print(result_string)  


#4

rows = 4
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (i * 2))


#5
age = int(input("გთხოვთ, შეიყვანოთ თქვენი ასაკი: "))


if age > 12:
    print("შენ არ ხარ 12 წლის")

