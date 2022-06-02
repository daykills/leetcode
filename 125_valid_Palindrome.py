""""
understand:
1. is the input only a string
2. is the element of the string only numbers and letters?
3. what shall be returned if the input is null?

input:""
output: true

input:"he,e,h"
output:true

input: "12, f, f, 2,1"
output: true

match: string +  Palindrome = two pointer

plan:
. edge case
1. establish two pointer: the left -> first element, the right -> last element
2. if the left pointer element not alphanumeric, keep move it to the right
3. if the right pointer element not alphanumeric, keep move it to the left
4. if left and right pointer element are alphanumeric and they are the same, keep both pointers to the centers, and repeat; else return False
5. return True if both pointers are cross or are in the same position
                       
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:return True
        l = 0
        r = len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
                