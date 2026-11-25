class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string)) + '#' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        start = 0
        while start < len(s):
            i = start
            while s[i]!='#':
                i += 1
            length = int(s[start:i])
            chunk = s[i+1:i+length+1]
            decoded_string.append(chunk)
            start = i + length + 1
        return decoded_string
