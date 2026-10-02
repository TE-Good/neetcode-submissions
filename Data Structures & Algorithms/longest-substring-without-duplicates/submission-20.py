class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_size = 0

        for char in s:
            while char in char_set:
                char_set.remove(s[left])
                left +=1
            
            char_set.add(char)
            max_size = max(max_size, len(char_set))

        return max_size
        