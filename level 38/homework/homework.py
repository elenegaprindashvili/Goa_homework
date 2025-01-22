# 2)შექმენი ფაილი სადაც გამოიყენებ ყველა set ფუნქციას(.clear, .set) და ასე შემდეგ
# 3)შექმენი dictionary შენს შესახებ, შემდეგ გამოიტანე მხოლოდ key
# 4)შექმენი dictionary შენს შესახებ, შემდეგ გამოიტანე მხოლოდ value
# 5)შექმენი ფუნქცია AddToDatabase, რომლესაც არგუმენტად გადაეცემა სახელი, გვარი და ასაკი, შემდეგ ეს ინფორმაცია უნდა დააბატოთ dictionaryს და 


my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print("Add 6:", my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)


my_set.clear()
print("clear:", my_set)


my_set = {1, 2, 3, 4, 5}
another_set = {4, 5, 6, 7}
union_set = my_set.union(another_set)
print("Union of sets:", union_set)



my_set.remove(4) 
print("After remove 4:", my_set)