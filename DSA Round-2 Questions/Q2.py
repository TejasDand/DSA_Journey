""" Q2. Find Pivot Index """

class Solution:
    def pivotIndex(self, nums):
        left = 0
        right = sum(nums)

        for index, num in enumerate(nums): 
            right -= num
            # print(right)
            
            if left == right:
                return index
            left += num
            # print(left)
        return -1

arr = Solution()
result = arr.pivotIndex([1,7,3,6,5,6])
print(result)