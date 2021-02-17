

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start, end = 0, 0

        for i in range(len(s)):
            len_1 = self.expand_around_corner(s, i, i)
            len_2 = self.expand_around_corner(s, i, i + 1)
            length = max(len_1, len_2)

            if length > end - start + 1:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start : end + 1]


    def expand_around_corner(self, s, left, right):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1

        return right - left - 1


# NOTE: tc : O(n^2) but the above sol performs much better  
# reference pepcoding

#         dp = [ [False] * len(s) for _ in range(len(s)) ]
#         start_res, end_res = 0, 1

#         for start in range(len(s)):
#             i, j = 0, start

#             while j < len(s):
#                 if start == 0:
#                     dp[i][j] = True

#                 elif start == 1 and s[i] == s[j]:
#                     dp[i][j] = True

#                 elif s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1]

#                 if dp[i][j]:
#                     start_res, end_res = i, j + 1
                
#                 i, j = i + 1, j + 1

#         return s[start_res : end_res]

