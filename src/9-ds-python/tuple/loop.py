items = (1, 2, 5.5, ["a", "b", "c"], ("apple", "mango"))
for item in items:
    print(item, type(item))
items[3][0] = "uganada"
print(items)