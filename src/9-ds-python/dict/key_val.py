marks = {1: 77, 2: 76, 5: 62, 4: 78, 3: 65}
print(type(marks))
print(marks[3])
print("Makrs of roll number 4 is", marks[4])


marks = {1005: 75, 1003: 72, 1002: 70, 1001: 75, 1004: 77}
print(marks[1003])


marks = {"DH2001": 75, "DH1777": 72, "KH2050": 70}
print(marks["DH2001"])

dt = {}
print(dt)
print(type(dt))
dt[1] = "one"
print(dt)
dt[2] = "two"
print(dt)

dt = {"a": "A", "b": "B", "c": "C"}
print(dt["a"])
print(dt["b"])
print(dt["c"])
dt["d"] = "D"
print(dt["d"])