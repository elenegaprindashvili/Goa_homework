# 1
def sum_of_positives(numbers):
    return sum(num for num in numbers if num > 0)
numbers = [1, -4, 7, 12]
result = sum_of_positives(numbers)
print(result)

# 2

def square_sum(numbers):
    return sum(num ** 2 for num in numbers)
numbers = [1, 2, 2]
result = square_sum(numbers)
print(result)



# 3
def sum_array(a):
    sum = 0
    for i in a:
        sum += i

        
# 4
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5]
result = average(numbers)
print(result)



# 5
def count_positives_sum_negatives(arr):
    if (len(arr) == 0 ):
        return []
    count_of_positives = 0
    sum_of_negatives = 0
    
    for el in arr: 
        if el > 0:
            count_of_positives += 1
        else:
            sum_of_negatives += el
    return [count_of_positives, sum_of_negatives]




       