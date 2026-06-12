class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sequence = set(nums)


        for i in nums:
            if i - 1 not in sequence:
                length = 1
                while i + length in sequence:
                    length += 1
                longest = max(longest, length)
        return longest