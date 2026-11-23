class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.replace("?","")
        s = s.replace(".","")
        s = s.replace("'","")
        s = s.replace(",","")
        s = s.replace(":","")
        s = s.replace("!","")
        s = s.lower()
        print(s)
        if(s == s[::-1]): return True
        return False