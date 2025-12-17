""" Q3. Missing Number """

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        currentSum = sum(nums)
        supposeSum = 0
        
        for num in range(0, n+1):
            supposeSum += num
        
        return supposeSum - currentSum

arr = Solution()
result = arr.missingNumber([9,6,4,2,3,5,7,0,1])
print(result)