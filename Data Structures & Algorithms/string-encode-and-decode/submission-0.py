class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        start = 0
        while start < len(s):
            length = ''
            while s[start] != '#':
                length += s[start]
                start += 1
            length = int(length)
            if length < 1:
                decoded_list.append('')
            else:
                decoded_list.append(s[start+1: start+int(length)+1])
            start += int(length) + 1
        return decoded_list
