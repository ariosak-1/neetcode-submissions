class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        counts = {}

        for ch in nums:
            if ch not in counts:
                counts[ch] = 1
            elif ch in counts:
                return True

        return False
