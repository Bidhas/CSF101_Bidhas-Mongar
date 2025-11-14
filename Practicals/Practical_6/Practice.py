def insertion_sort(arr):
    for i in range(1, len(arr)):          # Step 1
        key = arr[i]                      # Step 2
        j = i - 1                         # Step 3
        while j >= 0 and arr[j] > key:    # Step 4
            arr[j+1] = arr[j]             # Step 5
            j -= 1
        arr[j+1] = key                    # Step 6
    return arr

data = [5, 3, 4, 1, 2]
print("Unsorted:", data)
print("Sorted:", insertion_sort(data))

def linear_search(arr,target):
    for i in range (len(arr)):
        if arr [i] == target:
            return i 
    return -1

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

def binary_search(arr,target):
    left , right = 0, len(arr)
    while left <= right:
        mid = left + right // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")
