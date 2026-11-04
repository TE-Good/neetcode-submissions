class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            num_delim_end = i
            while s[num_delim_end] != "#":
                num_delim_end += 1
            length = int(s[i:num_delim_end])
            res.append(s[num_delim_end + 1 : num_delim_end + 1 + length])
            i = num_delim_end + 1 + length
        return res