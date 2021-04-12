def distribute(seq,k):
    maximum = max(seq)
    minimum = min(seq)
    length= float(maximum) - float(minimum)
    cell_length = float(length)/k
    list1= [0 for i in range(k)]
    for i in seq:
        if minimum == i:
            list1[0]+=1
        elif maximum==i:
            list1[k-1]+=1
        else:
            list1[int((i-minimum)/cell_length)] +=1
    return list1



assert distribute([1.25 , 1 , 2 , 1.75], 2 ) == [2 , 2]