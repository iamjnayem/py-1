import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int(m) + 1
    for i in range(3, m, 2):
        if n % i == 0:
            return False
    return True


a = int(input('enter a number: '))
b = int(input('enter a number: '))
if a == b:
    if is_prime(a) == True:
        print(a, "is prime number")
    else:
        print(a, "is not a prime number")
else:
    if a < b:
        n1 = a
        n2 = b
    else:
        n1 = b
        n2 = a

    for i in range(n1, n2+1, 1):
        if is_prime(i):
            print(i, "is prime number")