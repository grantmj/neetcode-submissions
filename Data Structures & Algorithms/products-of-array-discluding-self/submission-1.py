class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        for i in range(n):
            result = 1
            for j in range(n):
                if j != i:
                    result *= nums[j]
            output[i] = result

        return output