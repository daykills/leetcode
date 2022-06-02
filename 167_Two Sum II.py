"""
understand:
1. is the input just array
2. is guaranteed to have a solution

match: sorted array, find the target sum -> two pointer

plan:
1. establish two pointer: left points to the first element, right points to the last element
2. compare the sum of left pointer element and right pointer element with the target, if the sum is larger than the target, then move the right pointer to the center
3. if not #2, move the left pointer to the center
4. repeat the #2 and #3 until we find a solution that the sum equals to the target
5. return [l+1, r+1]
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            sums = numbers[l] + numbers[r]
            if sums == target:
                return [l + 1, r + 1]
            elif sums > target:
                r -= 1
            else:
                l += 1
        