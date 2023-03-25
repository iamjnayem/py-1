def avg(li):
    total = sum(li)
    return total/(len(li))

def multiplication_table(n = 1):
    m = 1
    while m <= 10:
        print(n, "X",m, "=", n *m )
        m += 1

multiplication_table(5)
multiplication_table()
