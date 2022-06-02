"""
Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.

Examples:

Input: laboratory, rat
Output: true

Input: cat, meow
Output: false

"""

"""
understand:
Be sure that you clarify the input and output parameters of the problem:

Are both inputs only strings?
Can elements of the string be both characters and numbers?
Can the second string be larger than the first?
Time & Space considerations:
Best Case Time Complexity: O(n * m)
Best Case Space Complexity: O(1)

match: string -> two pointer

plan:
1-2 sentence summary: loop through the first string for an initial match. If we find one, check that match for a full substring match

1) edge check
2) loop through the first string
3) find a match to the first character of the second string
4) while there is a match, loop through both strings in parellel to ensure the match
5) if there is an entire match to the second string, return True
6) If the match breaks, continue searching the first string for an initial character match
7) if we make it to the end of the first string without a full match, there is no substring match -> return False


"""

def substring(s1, s2):
    if len(s2) < 1:
        return True
    
    for i in range(len(s1)):
        match_i = i 
        match_j = 0
        while match_i < len(s1) and match_j < len(s2) and s1[match_i] == s2[match_j]:
            match_i += 1
            match_j += 1
        if match_j + 1 == len(s2):
            return True
    return False