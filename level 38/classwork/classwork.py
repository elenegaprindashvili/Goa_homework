
def manual_difference(set1, set2):
    return set1 - set2
set1 = {1, 2, 3, 4}
set2 = {3, 4, 6}

result = manual_difference(set1, set2)
print(result)  




student1 = {
    "სახელი": "nini",
    "გვარი": "wereteli",
    "ასაკი": 14,
    "საშუალო ქულა": 8.5
}

student2 = {
    "სახელი": "nika",
    "გვარი": "jafaridze",
    "ასაკი": 16,
    "საშუალო ქულა": 9.2
}

print("მოსწავლე 1:")
for key, value in student1.items():
    print(f"{key}: {value}")

print("მოსწავლე 2:")
for key, value in student2.items():
    print(f"{key}: {value}") 






