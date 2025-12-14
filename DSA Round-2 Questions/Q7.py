""" Q7. Move all Negative elements to the left side. """

class Solution:
    def segregateElements(self, arr):
        temp = []

        for i in arr:
            if i < 0:
                temp.append(i)
        for i in arr:
            if i >= 0:
                temp.append(i)

        arr[:] = temp
        return arr

arr = Solution()
result = arr.segregateElements([1, -1, 3, 2, -7, -5, 11, 6])
print(result)