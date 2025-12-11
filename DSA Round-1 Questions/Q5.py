"""Q5. Print All 0’s and 1’s Separately:
Given an array containing 0s and 1s, print all the 0s first and then all the 1s"""

def zeros_and_ones(arr):

    for i in arr:
       if i == 0:
           print(i, end=" ")
    for j in arr:
        if j == 1:
            print(j, end=" ")

arr = [0, 1, 1, 0, 1, 0, 0, 2, 0, 1, 5, 0, 0, 1]
zeros_and_ones(arr)