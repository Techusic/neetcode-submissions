class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for value in strs:
            string += value + "~"
        return string
    
    def decode(self, s: str) -> List[str]:
        ls = []
        temp = ""
        for char in s:
            if char == "~":
                ls.append(temp)
                temp =""
            else:
                temp+=char
        return ls
