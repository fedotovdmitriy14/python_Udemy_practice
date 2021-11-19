# Array inversion indicates how far the array is from being sorted.
#
# Inversions are pairs of elements in array that are out of order.
#
# Examples
# [1, 2, 3, 4]  =>  0 inversions
# [1, 3, 2, 4]  =>  1 inversion: 2 and 3
# [4, 1, 2, 3]  =>  3 inversions: 4 and 1, 4 and 2, 4 and 3
# [4, 3, 2, 1]  =>  6 inversions: 4 and 3, 4 and 2, 4 and 1, 3 and 2, 3 and 1, 2 and 1
# Goal
# The goal is to come up with a function that can calculate inversions for any arbitrary array


def count_inversions(array):
    result = 0
    if len(array) == 1:
        return result
    for j in range(len(array)-1):
        for i in range(len(array)-j-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                result += 1
    return result


print(count_inversions([6,5,4,3,2,1]))