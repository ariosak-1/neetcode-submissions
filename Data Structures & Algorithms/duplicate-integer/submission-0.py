class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        counts = {}

        for i in range(len(nums)):

            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1

        for ch in counts:
            if counts[ch] > 1:
                return True
                
        return False
