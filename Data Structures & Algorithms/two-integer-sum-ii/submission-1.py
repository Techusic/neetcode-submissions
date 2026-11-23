class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ass = dict()
        for i in range(len(numbers)):
            ass.setdefault(target - numbers[i], i)

        for i in range(len(numbers)):
            if numbers[i] in ass and ass[numbers[i]] != i :

                return sorted([i+1, ass[numbers[i]]+1])


