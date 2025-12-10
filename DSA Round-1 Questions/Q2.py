"""2.Print Array Elements After Multiplying by 5:
Write a program that multiplies every element in the given array by 5 and prints the updated array"""

def print_array(arr):
    for e in arr:
        print(e*5)

lst = list(map(int, input("Enter numbers: ").split()))
print_array(lst)