def calculate_special_sum(n):
    sumdata = 0
    while n>=1:
        sumdata += ((n - 1) ** 2) * n
        n=n-1
    return sumdata


if __name__ == '__main__':

    assert calculate_special_sum ( 3 ) == 14


