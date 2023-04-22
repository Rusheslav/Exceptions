def sum_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Массивы разной длины"
    arr3 = [None] * len(arr1)
    for i in range(len(arr1)):
        if type(arr1[i]) != int or type(arr2[i]) != int:
            return "Не все значения в массивах - целые числа"
        arr3[i] = arr1[i] + arr2[i]
    return arr3


print(sum_arrays([1, 2, 3], [4, 5, 6]))
