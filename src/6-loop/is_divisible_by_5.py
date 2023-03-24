result = 0
for num in range(101):
    if num % 5 == 0:
        print(num)
        result += num 

print("Sum is", result)

result = 0
for num in range(5, 101, 5):
    result += num 

print("sum is", result)