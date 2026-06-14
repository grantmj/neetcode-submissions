class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sequence = set(nums)

        for i in nums:
            length = 1
            while length + i in sequence:
                length += 1
            longest = max(longest, length)
        return longest