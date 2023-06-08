class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t): 
            lst1 = sorted(list(s))
            lst2 = sorted(list(t))
            if lst1 == lst2: 
                return True
            else: 
                return False
        else: 
            return False