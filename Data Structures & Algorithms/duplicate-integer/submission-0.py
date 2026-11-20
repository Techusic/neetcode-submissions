class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        add = set()
        for val in nums:
            if val in add:
                return True
            add.add(val)
        return False