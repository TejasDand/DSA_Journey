"""Q4. Find Minimum and Maximum in an Array:
Write a program to find the smallest (min) and largest (max) number in the array"""

def min_and_max(arr):

    max_val = arr[0]
    min_val = arr[0]

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
    
    print(f'Maximum value: {max_val}')
    print(f'Minimum value: {min_val}')

arr = [10, 20, 12, 30, 60, 42, 8, 45, 3, 74, 15, 69]
min_and_max(arr)