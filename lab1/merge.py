def merge(num1,num2):
    list2 = list(num1+num2)

    def quickSort( nums):
            if (len(nums) == 0):
                return []
            if (len(nums) == 1):
                return nums
            flag = nums[0]
            left = []
            right = []
            for i in range(1, len(nums)):
                if nums[i] > flag:
                    right.append(nums[i])
                else:
                    left.append(nums[i])
            left = quickSort(left)
            right = quickSort(right)

            return left + [flag] + right

    if isinstance(num1,list):
        return quickSort(list2)
    else:
        return tuple(quickSort(list2))




assert merge ([1 , 2 , 7], [3]) == [1 , 2 , 3 , 7]
assert merge (( 3 , 15 ) , (7 , 8 ) ) == (3 , 7 , 8 , 15 )

