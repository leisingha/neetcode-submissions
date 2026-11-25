class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''
        for ch in s:
            if ch.isalnum():
                clean_s += ch.lower()

        for i, j in zip(range(len(clean_s)), range(len(clean_s)-1, -1, -1)):
            if clean_s[i] != clean_s[j]:
                return False
        return True
        