class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        boob = sorted(nums)
        boobs = set()
        for i in range(len(boob)):
            j = i+1
            k = len(boob)-1

            while j < k:
                if boob[k] + boob[j] == -boob[i]:
                    boobs.add(tuple([boob[i],boob[j],boob[k]]))

                if boob[k] + boob[j] >= -boob[i]:
                    k = k-1
                if boob[k] + boob[j] < -boob[i]:
                    j = j+1

        boobs = list(boobs)
        return boobs