class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ass = [1] * len(nums)
        boob = [1] * len(nums)
        waist = []
        for i in range(1, len(nums)):
            ass[len(nums)-i-1] = ass[len(nums)-i] * nums[len(nums)-i]
            boob[i] = boob[i-1]*nums[i-1]
        
        for i in range(0, len(nums)):
            waist.append(ass[i]*boob[i]) 
        
        return waist