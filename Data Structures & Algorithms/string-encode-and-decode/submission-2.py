class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strings = ''
        for string in strs:
            encoded_strings += str(len(string)) + '#' + string
        return encoded_strings


    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != '#':
                i = i + 1
            length = int(s[start:i])
            chunk = s[i+1:i+length+1]
            decoded_strings.append(chunk)
            i = i + length + 1
        return decoded_strings

                
            
                
            
        
