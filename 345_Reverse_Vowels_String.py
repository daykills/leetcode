class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        arr = list(s)
        
        while l < r:
            if arr[l].lower() not in 'aeiou':
                l += 1
                continue
            if arr[r].lower() not in 'aeiou':
                r -= 1
                continue
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return ''.join(arr)
