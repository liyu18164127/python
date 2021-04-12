def get_primes(n):
    import math
    num = []
    a = []
    for i in range(0, n + 1):
        a.append(1)
    for i in range(0, n + 1):
        if i % 2 == 0:
            a[i] = 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        if (a[i] == 1):
            for j in range(i + i, n + 1, i):

                a[j] = 0

    a[2] = 1
    for i in range(2, n + 1):
        if a[i] == 1:
            num.append(i)

    return num



assert [2 , 3 , 5 , 7 , 11] == sorted ( get_primes ( 11 ) )