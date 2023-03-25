# Hello Test! 123 123, good.
str = input()
p1 = [i for i in str if 65 <= ord(i) <= 90]
print(''.join(p1))

p2 = [i for i in str if 97 <= ord(i) <= 122]
print(''.join(p2))

p3 = [i for i in str if 48 <= ord(i) <= 57]
print(''.join(p3))

p4 = [i for i in str if (not (65 <= ord(i) <= 90) and not (97 <= ord(i) <= 122) and not (48 <= ord(i) <= 57))]
print(''.join(p4))
