class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26
            
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        result = []
        for value in groups.values():
            result.append(value)

        return result
        