fruits = ['apple', 'mango', 'coconut', 'banana', 'orange']
fruits.remove('coconut')
print(fruits)
#raise exeception
#fruits.remove('abcd')

item = 'lalalala'
if item in fruits:
    fruits.remove(item)
else:
    print(item, 'not in the list')