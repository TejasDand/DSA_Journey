"""Q3. Find the Target in the Array:
Write a program to find whether a given target value exists in the array or not."""

def target_finding_arr(arr, target):
    for e in range(len(arr)):
        
        if arr[e] == target:
            print(f"Target found at lst[{e}].")
            return
    print("Target not found!")
    

lst = [10, 40, 74, 30, 19]
target = int(input("\nEnter a number you want to find numbers list: "))

target_finding_arr(lst, target)