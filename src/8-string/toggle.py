str = input()
str_len = len(str)
loop_count = str_len // 2
j = 0
result = ''

for i in range(loop_count):
    result += str[j+1] + str[j]
    j += 2
print(result)
