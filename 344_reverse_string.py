"""
understand: 
1. is input only a array
2. what should be returned if the input is null
3. is element of the array ascii character?

['a','b']
[' ', 'b' ]
['']

match: 
1. reverse -> two pointer

plan:
1. establish two pointers: left on the first element and right one the last element of the array
2. swap both elements pointed by the left/right pointers
3. move both pointers one index closer to the center of the array
4. repeat until both pointers cross or are in the same position
5. return the original input

Time Complexity: O(n)
Space Complexity: O(1)

left = 0
right = len(input array) - 1

while left < right:
    swap left and right
    left ++
    right --

return the input
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        