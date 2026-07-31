class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output


    def decode(self, s: str) -> List[str]:
        result = []
        loop_start_index = 0

        while loop_start_index != len(s):
            current_index = loop_start_index
            while s[current_index] != "#":
                current_index +=1
            
            length_of_word = int(s[loop_start_index:current_index])
            word_start_index = current_index + 1
            word_end_index = word_start_index + length_of_word

            result.append(s[word_start_index: word_end_index])

            loop_start_index = word_end_index

        return result

