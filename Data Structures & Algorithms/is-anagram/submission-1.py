class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = 0

        if len(s) != len(t):
            return False

        for ch in t:
            if ch in s and t.count(ch) == s.count(ch):

                count+=1

        if count == len(t):
            return True
        else:
            return False
        
                