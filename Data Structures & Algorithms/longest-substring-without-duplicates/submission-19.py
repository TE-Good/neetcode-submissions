class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        length = 0

        for char in s:
            while char in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(char)
            length = max(length, len(char_set))

        return length
        