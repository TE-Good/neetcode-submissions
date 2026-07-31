class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_hash[s[i]] += 1
            t_hash[t[i]] += 1

        return s_hash == t_hash