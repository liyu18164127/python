def compress(seq):
    a={}
    for i in seq:

        if i in a.keys():
            a[i] = a[i] +1
        else:
            a[i] = 1
    return [(int(key),value)for key,value in a.items()]



if __name__ == '__main__':

    expected_sorted = [(1, 2), (2, 1), (3, 1)]
    actual_sorted = sorted(compress([1, 2, 1, 3]))
    assert expected_sorted == actual_sorted