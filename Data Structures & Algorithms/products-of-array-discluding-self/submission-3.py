class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ass = [1] * len(nums)
        boob = 1 
        waist = 1
        for i in range(len(nums)):
            ass[i] = boob
            boob *= nums[i] 
        
        for i in range(len(nums)):
            ass[len(nums)-i-1] *= waist
            waist *= nums[len(nums)-i-1]
        
        return ass