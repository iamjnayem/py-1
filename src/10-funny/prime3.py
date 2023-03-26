import math
import timeit

def is_prime3(n = 1023):
    if n == 2:
        return True
    if n % 2 == 0:
        print(n, "is divisible by 2")
        return False
    if n < 2:
        return False

    prime = True
    m = n // 2 + 1
    for x in range(3, m, 2):
        if n % x == 0:
            # print(n, "is divisible by ", x)
            prime = False
            return prime
    return prime



def is_prime4(n = 1023):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    m = math.sqrt(n)
    m = int(m) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True


t1 = timeit.timeit(is_prime3)
t2 = timeit.timeit(is_prime4)
print(t1, t2, t1/t2)