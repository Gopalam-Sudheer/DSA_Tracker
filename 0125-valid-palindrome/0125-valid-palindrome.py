class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0
        end=len(s)-1
        while start<=end:
            while start<end and not (s[start].isalpha() or s[start].isnumeric()):
                start+=1
            while start<end and not (s[end].isalpha() or s[end].isnumeric()):
                end-=1
            if start<=end and s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        return True
            