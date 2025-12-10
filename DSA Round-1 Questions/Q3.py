"""Q3. Find the Target in the Array:
Write a program to find whether a given target value exists in the array or not."""

def target_finding_arr(arr, target):
    for e in arr:
        
        if e == target:
            print(f"Target found at lst[{arr.index(e)}].")
            return
    print("Target not found!")
    

lst = list(map(int, input("Enter numbers: ").split()))
target = int(input("\nEnter a number you want to find in your given numbers list: "))

target_finding_arr(lst, target)