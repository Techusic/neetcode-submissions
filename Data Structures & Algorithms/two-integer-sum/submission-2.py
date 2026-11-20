class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sa = dict()
        i=0
        for val in nums:
            sa.setdefault(target - val, i)
            i+=1
        for i in range(1, len(nums)):
            if nums[i] in sa and sa[nums[i]] != i:
                return sorted([sa[nums[i]], i])
         