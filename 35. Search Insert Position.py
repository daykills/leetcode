"""
look for lower bound

"""
#brute force
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i 
        return len(nums)

#binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        
        while l < r:
            mid = (r - l) // 2 + l
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l