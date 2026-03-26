class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Approach:
    - If the lengths of the strings differ, they cannot be anagrams.
    - Use a hashmap (dictionary) to store the frequency of each character in string `s`.
    - Traverse string `t` and decrement the corresponding character counts.
    - If a character in `t` is not found in the hashmap or its count goes negative,
      the strings are not anagrams.
    - If all counts balance out, the strings are valid anagrams."""
        if len(s) != len(t):
            return False
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch,0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True

        