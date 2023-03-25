li = [1, 2, 3, 4]
new_li = []
for x in li:
    new_li.append(2 * x)

print(new_li)

#list comprehension
new_li = [2 * x for x in li]
print(new_li)


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for x in li:
    if x % 2 == 0:
        even_numbers.append(x)


print(even_numbers)

even_numbers = [x for x in li if x % 2 == 0]
print(even_numbers)


li = [1, 2, 3, 4]
squre_list = [x**2 for x in li]
print(squre_list)