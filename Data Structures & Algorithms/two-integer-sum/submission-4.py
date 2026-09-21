class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in prevMap:
                return [prevMap[compliment], i]
            
            prevMap[nums[i]] = i