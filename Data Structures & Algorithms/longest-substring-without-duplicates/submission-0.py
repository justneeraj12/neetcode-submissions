class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        L = 0
        longest_sequence = 0

        for R, char in enumerate(s):

            if char in seen:

                L = max(L, seen[char] + 1)

            seen[char] = R

            current_length = (R - L) + 1
            longest_sequence = max(longest_sequence, current_length)
            
        return longest_sequence
        