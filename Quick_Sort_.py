
# this is use list slicing: and use recursion for Quick Sort

def Quick_sort(data_list):
    n = len(data_list)
    if n <=1:
        return data_list
    else:
        pivot = data_list[0]
        lesser = [ x for x in data_list[1:] if x <= pivot]
        greater = [ x for x in data_list[1:] if x>pivot]
        return Quick_sort(lesser) + [pivot] + Quick_sort(greater)
    
nums = input("Enter integers separated by spaces: ")
data = list(map(int, nums.split()))
data = Quick_sort(data)
print(data)






## Removed list slicing

def Quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    pivot = data_list[0]
    lesser = []
    greater = []
    
    # Iterate through the list once to separate the values
    for x in data_list[1:]:
        if x <= pivot:
            lesser.append(x)
        else:
            greater.append(x)
    
    # Recursively sort and combine the results
    return Quick_sort(lesser) + [pivot] + Quick_sort(greater)

nums = input("Enter integers separated by spaces: ")
data = list(map(int, nums.split()))
data = Quick_sort(data)
print(data)






## This is use stack 

def Quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list

    stack = [(0, len(data_list) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(data_list, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return data_list

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

nums = input("Enter integers separated by spaces: ")
data = list(map(int, nums.split()))
data = Quick_sort(data)
print(data)



