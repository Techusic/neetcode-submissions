class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        b = set()
        count = 0
        b.add(count)
        count = 1
        for val in a:
            if val-1 not in a:
               while True :
                    if val+1 in a:
                        count +=1
                        val = val+1
                    else:
                        b.add(count)
                        count = 1
                        break
        return(max(b))