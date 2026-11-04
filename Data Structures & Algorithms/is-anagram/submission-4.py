class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_alphas = [0] * 26
        t_alphas = [0] * 26

        for char in s:
            char_num = ord(char) - ord("a")
            s_alphas[char_num] += 1
        for char in t:
            char_num = ord(char) - ord("a")
            t_alphas[char_num] += 1

        return s_alphas == t_alphas
