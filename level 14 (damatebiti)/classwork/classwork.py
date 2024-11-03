name = "Two Tower"
result = ""

for i in name:
    result += i

print(result)



number = int(input("8"))

if number % 2 == 0:
    print(f"{number} არის ლუწი.")
else:
    print(f"{number} არის კენტი.")
    
    
   
    for i in range(1, 101):
     if i % 2 == 0:
        print(f"{i} არის ლუწი.")
    else:
        print(f"{i} არის კენტი.")

        for i in range(1, 101):    
         if i % 2 == 0:
           print(f"{i} არის ლუწი.")
    
         print(f"{i} არის კენტი.")
