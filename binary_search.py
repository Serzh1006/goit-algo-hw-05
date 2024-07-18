def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    upper_edge = None
    iterations = 0

    while left <= right:
        iterations+=1
        mid = (left + right)//2
        
        if target < arr[mid]:
            upper_edge = arr[mid]
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            return (iterations, upper_edge)
    return (iterations, upper_edge)


list_num = [1.2, 2.5, 3.5, 4.5, 5.2, 6.2, 6.7, 8.5, 9.4, 10.1]
target = 4

result = binary_search(list_num, target)
print(result)