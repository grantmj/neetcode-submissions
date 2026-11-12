class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSub = 0

        for num in nums:
            if currentSub < 0:
                currentSub = 0
            currentSub += num
            maxSub = max(maxSub, currentSub)
        return maxSub