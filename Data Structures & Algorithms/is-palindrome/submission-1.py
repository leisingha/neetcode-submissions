class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        for i, j in zip(range(len(cleaned)), reversed(range(len(cleaned)))):
            if cleaned[i] != cleaned[j]:
                return False
        return True