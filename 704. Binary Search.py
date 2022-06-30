"""
understand:
sorted array, unique values

match:
binary search

plan:
[a, )

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) 
        
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return -1