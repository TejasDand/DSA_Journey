"""Q1. Print an Array:
Write a program that takes an array as input and prints all its elements."""

def print_arr(arr):
    for e in arr:
        print(e)

lst = list(map(int, input("Enter numbers: ").split()))
print_arr(lst)