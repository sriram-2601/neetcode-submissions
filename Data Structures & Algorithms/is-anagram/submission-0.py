class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a=[0]*26
        for i in s:
            a[ord(i)-ord('a')]+=1
        for i in t:
            a[ord(i)-ord('a')]-=1    
        for c in a:
            if c!=0:
                return False
        return True        
        