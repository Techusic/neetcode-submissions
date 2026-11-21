class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ass = dict(Counter(nums))
        les = []
        for i in range(0,k):
            a = max(ass, key = lambda x : ass[x])
            les.append(a)
            ass.pop(a)
            
        return les
        