class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for ch in t:
            if ch not in s:
                return False

            if t.count(ch) != s.count(ch):
                return False

        return True
                