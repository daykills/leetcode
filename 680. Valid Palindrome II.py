"""
understand:
1. is input only string
2. is element only letters/lowercase
3. what is output if the input is null

example:
"a" -> True
"abb" -> True

match: two pointer

plan:
1. establish two pointer: left -> start, right -> end of the input string
2. if s[left] == s[right]: move two pointers towards to the center
3. repeat #2
4. determine if only move one pointer to center will make the string palidrome
5. if input is palidrome, then two pointers will on the same position or will be crossed, return True

"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return s[l + 1: r + 1] == s[l + 1: r + 1][::-1] or s[l: r] == s[l:r][::-1]
            
        return True
