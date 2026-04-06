class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Approach: Expand Around Center
        - A palindrome mirrors around its center.
        - For each index, treat it as a center and expand outward to check for palindromes.
        - Handle two cases:
         1. Odd length palindrome → center at one character (l = i, r = i)
         2. Even length palindrome → center between two characters (l = i, r = i+1)
         - Expand while characters match and stay within bounds.
         - Track the longest substring found during expansion."""

        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

            
                
        