class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ""
        for st in strs:
            output += str(len(st)) + "#" + st
        return output

    def decode(self, s: str) -> List[str]:
        output = []

        length_start = 0
        while length_start < len(s):
            length_end = length_start
            while s[length_end] != "#":
                length_end += 1

            length = int(s[length_start:length_end])
            output.append(s[length_end + 1 : length_end + length + 1])

            length_start = length_end + length + 1
        
        return output