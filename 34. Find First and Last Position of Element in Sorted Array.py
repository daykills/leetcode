"""
look for first and last value in the array equal to the target. 
return -1 if the target is not in the array

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = self.lower_bound(nums, target)
        upper = self.upper_bound(nums, target)
        return [lower, upper] 
    
    def lower_bound(self, nums, target):
        l = 0
        r = len(nums)
        
        while l < r:
            mid = (r - l) // 2 + l
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l if target in nums else -1
    
    
    def upper_bound(self, nums, target):
        l = 0
        r = len(nums)
        
        while l < r:
            mid = (r - l) // 2 + l
            if target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l - 1 if target in nums else -1
    