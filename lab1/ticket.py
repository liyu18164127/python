def get_nearest_lucky_ticket(number):

    def left(number):
        list1 = []
        for i in str(number):
            list1.append(i)
        even = []
        odd = []
        for i in list1[::2]:
            even.append(int(i))
        for i in list1[1::2]:
            odd.append(int(i))
        sumeven = sum(even)
        sumodd = sum(odd)
        if sumeven == sumodd:
            return number
        else:
            return left(number - 1)

    def right(number):
        list1 = []
        for i in str(number):
            list1.append(i)
        even = []
        odd = []
        for i in list1[::2]:
            even.append(int(i))
        for i in list1[1::2]:
            odd.append(int(i))
        sumeven = sum(even)
        sumodd = sum(odd)
        if sumeven == sumodd:
            return number
        else:
            return right(number + 1)
    if abs(left(number) - number)> abs(right(number) - number):
            return right(number)
    else:
            return left(number)

assert get_nearest_lucky_ticket ( 111111 ) == 111111
assert get_nearest_lucky_ticket ( 123321 ) == 123321
assert get_nearest_lucky_ticket ( 123320 ) == 123321
assert get_nearest_lucky_ticket ( 333999 ) == 334004