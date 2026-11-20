class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ass = dict()
        for item in strs:
            if item in ass:
                ass.setdefault(str(sorted(item)), str(item))
            else:
                ass.setdefault(str(sorted(item)), []).append(item)
                
        butt = []

        for value in ass.values():
            butt.append(value)
        return butt