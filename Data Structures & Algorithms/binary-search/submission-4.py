class Solution:
    def BinarySearch(self, l: int, r: int, nums: List[int], target: int) -> int:
        while l > r:
            return -1
        mid = l + ( (r- l) // 2)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.BinarySearch(mid + 1,r, nums, target)
        return self.BinarySearch(l, mid - 1, nums, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.BinarySearch(0, len(nums) - 1, nums, target)
    
        