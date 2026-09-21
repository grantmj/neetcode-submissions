class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Map = set()

        for num in nums:
            if num in Map:
                return True
            Map.add(num)
        return False