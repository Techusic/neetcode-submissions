class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ass = set(nums)
        boob = set()
        count = 0
        boob.add(count)
        count = 1
        for val in ass:
            if val-1 not in ass:
               while True :
                    if val+1 in ass:
                        count +=1
                        val = val+1
                    else:
                        boob.add(count)
                        count = 1
                        break
        return(max(boob))