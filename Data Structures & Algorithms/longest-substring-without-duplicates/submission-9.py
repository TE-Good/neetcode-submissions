class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        longest = 0

        for char in s:
            while char in window:
                window.remove(s[l])
                l += 1
            
            window.add(char)
            longest = max(longest, len(window))

        return longest
